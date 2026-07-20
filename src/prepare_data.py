import pandas as pd

# ==========================
# Load the datasets
# ==========================
fake_df = pd.read_csv("data/Fake.csv")
true_df = pd.read_csv("data/True.csv")

# ==========================
# Add labels
# Fake = 0
# Real = 1
# ==========================
fake_df["label"] = 0
true_df["label"] = 1

# ==========================
# Combine the datasets
# ==========================
df = pd.concat([fake_df, true_df], ignore_index=True)

# ==========================
# Shuffle the dataset
# (Very important before training)
# ==========================
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# ==========================
# Display information
# ==========================
print("=" * 60)
print("Combined Dataset")
print("=" * 60)

print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nLabel Distribution:")
print(df["label"].value_counts())

print("\nColumns:")
print(df.columns)

# ==========================
# Save the prepared dataset
# ==========================
df.to_csv("data/news.csv", index=False)

print("\nDataset saved successfully!")
print("Location: data/news.csv")