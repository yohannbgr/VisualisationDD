# Projet - Analyse d'un portefeuille de crédit

## Description
Analyse d'un portefeuille fictif de 44 991 emprunteurs issu d'un dataset Kaggle. Le projet couvre le nettoyage et l'enrichissement de la base en Python, puis la création de cinq tableaux de bord Tableau Public pour explorer le profil des emprunteurs, le risque de crédit, les caractéristiques des prêts, la performance et la segmentation financière.

La principale valeur ajoutée du projet est la reconstruction de la variable `categorie_score_credit` à partir du ratio d'endettement, qui transforme une segmentation non discriminante (taux de défaut uniforme à 22 %) en un outil opérationnel révélant un rapport de 1 à 6,4 entre les catégories extrêmes (11,8 % à 75,4 %).

## Visualisation Tableau Public

| # | Dashboard | Lien |
|---|-----------|------|
| 1 | Profil des emprunteurs | (https://public.tableau.com/app/profile/yohann.bogaert/viz/ProjetEmpruntsBancaires/Profildesemprunteurs) |
| 2 | Analyse du risque de crédit |(https://public.tableau.com/app/profile/yohann.bogaert/viz/ProjetEmpruntsBancaires/Profildesemprunteurs) |
| 3 | Analyse des prêts | (https://public.tableau.com/app/profile/yohann.bogaert/viz/ProjetEmpruntsBancaires/Profildesemprunteurs) |
| 4 | Performance et défauts | (https://public.tableau.com/app/profile/yohann.bogaert/viz/ProjetEmpruntsBancaires/Profildesemprunteurs) |
| 5 | Segmentation financière | (https://public.tableau.com/app/profile/yohann.bogaert/viz/ProjetEmpruntsBancaires/Profildesemprunteurs) |

## Rapport

[rapport_dashboard_credit_v3]

## Technologies
- Python (pandas, numpy)
- Tableau Public
- Jupyter Notebook

## Structure du dépôt
- `nettoyage_base_final.ipynb` — notebook de nettoyage et d'enrichissement
- `data/base_final_uptated.csv` — base enrichie (44 991 lignes, 22 colonnes)

## Lancer le code
```bash
pip install -r requirements.txt
jupyter notebook nettoyage_base_final.ipynb
```