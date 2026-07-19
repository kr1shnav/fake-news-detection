import shutil
from pathlib import Path

import kagglehub

# Download dataset
dataset_path = Path(
    kagglehub.dataset_download("clmentbisaillon/fake-and-real-news-dataset")
)

print(f"Dataset downloaded to: {dataset_path}")

# Project root (parent of the src folder)
project_root = Path(__file__).resolve().parent.parent

destination = project_root / "data"
destination.mkdir(exist_ok=True)

# Copy CSV files
for csv_file in dataset_path.glob("*.csv"):
    shutil.copy2(csv_file, destination)
    print(f"Copied: {csv_file.name}")

print(f"\nDataset copied to: {destination}")