import pandas as pd

# Load datasets
fake_df = pd.read_csv("data/Fake.csv")
true_df = pd.read_csv("data/True.csv")

print("=" * 50)
print("FAKE NEWS DATASET")
print("=" * 50)
print(fake_df.head())

print("\n")

print("=" * 50)
print("TRUE NEWS DATASET")
print("=" * 50)
print(true_df.head())

print("\nFake Dataset Shape:", fake_df.shape)
print("True Dataset Shape:", true_df.shape)

print("\nFake Dataset Info")
print(fake_df.info())

print("\nTrue Dataset Info")
print(true_df.info())

print("\nMissing Values (Fake)")
print(fake_df.isnull().sum())

print("\nMissing Values (True)")
print(true_df.isnull().sum())