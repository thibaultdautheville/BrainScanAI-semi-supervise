import os
from pathlib import Path

# ---------------------- Chemins du projet ---------------------
# Chemins relatifs à la racine du dépôt : le même code tourne sur le Mac et sur la VM.
# DATA_PATH peut être surchargé par variable d'environnement si les données sont ailleurs.
PROJECT_PATH = Path(__file__).resolve().parents[1]
DATA_PATH = Path(os.getenv("DATA_PATH", PROJECT_PATH / "data"))
RAW_DATA_PATH = DATA_PATH / "raw" / "mri_dataset_brain_cancer_oc"  # contenu du zip fourni par Clara
PROCESSED_DATA_PATH = DATA_PATH / "processed"  # sorties des notebooks (features, labels faibles...)
FIGURES_PATH = PROJECT_PATH / "reports" / "figures"
MODELS_PATH = PROJECT_PATH / "models"  # poids des CNN entraînés (non versionnés)

# ---------------------- Dossiers d'images ---------------------
LABELED_PATH = RAW_DATA_PATH / "avec_labels"  # 2 sous-dossiers : cancer/ et normal/ (le label = nom du dossier)
UNLABELED_PATH = RAW_DATA_PATH / "sans_label"  # images sans étiquette

# ---------------------- Paramètres techniques ---------------------
random_state = 42  # graine unique pour toute la reproductibilité (numpy, torch, scikit-learn)
