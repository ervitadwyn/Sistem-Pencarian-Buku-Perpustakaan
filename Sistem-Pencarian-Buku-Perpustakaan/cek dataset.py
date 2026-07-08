import pandas as pd

df = pd.read_excel("Buku Induk Perpustakaan copy.xlsx")

print(df.head())

print("\n====================")

print(df.dtypes)

print("\n====================")

print(df["Salin"].unique())