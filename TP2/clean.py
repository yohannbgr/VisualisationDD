#!/usr/bin/env python3
import argparse
import pandas as pd


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoyage principal :
    - supprime doublons exacts
    - nettoie Start Year (retire 'Year' / 'AD' puis convertit en numérique)
    - crée Decennie et Has_Deaths
    - sélectionne et renomme colonnes pour Tableau
    """

    # 1) Doublons exacts
    df = df.drop_duplicates()

    # 2) Correction Start Year
    if "Start Year" in df.columns:
        s = df["Start Year"].astype(str)
        s = s.str.replace("Year", "", regex=False)
        s = s.str.replace("AD", "", regex=False)
        s = s.str.strip()
        df["Start Year"] = pd.to_numeric(s, errors="coerce")

    # 3) Colonnes utiles
    if "Start Year" in df.columns:
        df["Decennie"] = (df["Start Year"] // 10) * 10

    if "Total Deaths" in df.columns:
        df["Has_Deaths"] = df["Total Deaths"] > 0

    # 4) Sélection + renommage pour export (adapte si tes noms diffèrent)
    cols_wanted = [
        "ID_Catastrophe",
        "Type_Catastrophe",
        "Country",
        "Region",
        "Start Year",
        "Decennie",
        "Total Deaths",
        "Has_Deaths",
    ]
    cols_present = [c for c in cols_wanted if c in df.columns]
    df_export = df[cols_present].copy()

    df_export = df_export.rename(columns={
        "Start Year": "Start_Year",
        "Total Deaths": "Deces",
    })

    # noms sans espaces au cas où
    df_export.columns = df_export.columns.str.strip().str.replace(" ", "_", regex=False)

    return df_export


def build_profile(df: pd.DataFrame, html_path: str) -> None:
    """
    Génère un rapport de qualité HTML.
    Selon l'environnement, la lib peut s'appeler pandas_profiling ou ydata_profiling.
    """
    try:
        from pandas_profiling import ProfileReport
    except ImportError:
        from ydata_profiling import ProfileReport

    profile = ProfileReport(df, title="Rapport de qualité")
    profile.to_file(html_path)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Nettoyage CatNat -> export CSV prêt pour Tableau (+ profiling optionnel)"
    )
    parser.add_argument("-i", "--input", required=True, help="Chemin du fichier d'entrée (CSV)")
    parser.add_argument("-o", "--output", default="catnat_clean.csv", help="Chemin du CSV de sortie")
    parser.add_argument("--profile", action="store_true", help="Active la génération du rapport HTML")
    parser.add_argument("--profile-out", default="rapport_qualite.html", help="Chemin du rapport HTML")
    return parser.parse_args()


def main():
    args = parse_args()

    # Lecture
    df = pd.read_csv(args.input)

    # Nettoyage
    df_clean = clean_dataframe(df)

    # Vérif finale demandée
    print(df_clean.info())
    print(df_clean.head())

    # Export
    df_clean.to_csv(args.output, index=False, encoding="utf-8")
    print(f"Export OK -> {args.output}")

    # Profiling optionnel
    if args.profile:
        build_profile(df_clean, args.profile_out)
        print(f"Profiling OK -> {args.profile_out}")


if __name__ == "__main__":
    main()
