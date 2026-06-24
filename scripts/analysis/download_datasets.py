"""Descarga datasets UCI para experimentos Widrow."""
import pandas as pd
from pathlib import Path

datasets_dir = Path("data/raw/datasets")
datasets_dir.mkdir(parents=True, exist_ok=True)

# Wine Quality
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=";")
df.to_csv(datasets_dir / "winequality-red.csv", index=False)
print(f"🍷 Wine Quality: {df.shape[0]} filas, {df.shape[1]} columnas")
print(f"   Features: {list(df.columns[:-1])}")
print(f"   Target (quality): {sorted(df['quality'].unique())}")
print(f"   Buen vino (>=7): {sum(df['quality'] >= 7)} / {len(df)} ({100*sum(df['quality'] >= 7)/len(df):.1f}%)")
print("   ✅ Listo")
