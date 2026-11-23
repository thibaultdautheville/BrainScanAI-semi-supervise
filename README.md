# BrainScanAI : analyse semi-supervisée d'IRM cérébrales

Projet 7 OpenClassrooms (parcours Data Scientist Machine Learning), **Option B** : « Analysez des images médicales avec des méthodes semi-supervisées », pour la startup fictive CurelyticsIA.

## Mission

Un jeu de 1 506 IRM cérébrales, dont seulement 100 étiquetées par des radiologues (50 « cancer », 50 « normal »). Objectifs :

1. explorer les images et extraire des caractéristiques visuelles avec un modèle pré-entraîné (type ResNet) ;
2. appliquer des méthodes de clustering pour repérer des regroupements naturels et produire une labellisation « faible » ;
3. mettre en œuvre une méthode semi-supervisée qui exploite les labels partiels, et la comparer à un apprentissage supervisé ;
4. formuler des recommandations pour un passage à l'échelle (4 millions d'images, budget de 5 000 €).

## Organisation du dépôt

```
├── data/                               # NON versionné (.gitignore)
│   ├── raw/mri_dataset_brain_cancer_oc/  #   contenu du zip fourni (avec_labels/{cancer,normal}, sans_label/)
│   └── processed/                      #   features extraites, labels faibles
├── notebooks/
│   ├── 01_analyse_non_supervisee.ipynb # Livrable 1 : étapes 1 à 3 (exploration, features, clustering)
│   └── 02_approche_semi_supervisee.ipynb # Livrable 2 : étape 4 (à venir)
├── src/settings.py                     # chemins et constantes (relatifs à la racine du dépôt)
├── reports/figures/                    # graphiques produits par les notebooks
├── models/                             # NON versionné : poids des CNN entraînés
├── pyproject.toml / uv.lock            # environnement (uv, Mac)
└── requirements.txt                    # même environnement pour pip (VM)
```

## Installation

### Mac (uv)

```bash
uv sync
uv run python -m ipykernel install --user --name projet7 --display-name "Python (Projet 7)"
```

Puis choisir le noyau « Python (Projet 7) » dans le notebook.

### Autre machine (pip)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Données

Décompresser `mri_dataset_brain_cancer_oc.zip` dans `data/raw/`. Si les données sont rangées ailleurs, définir la variable d'environnement `DATA_PATH`.
