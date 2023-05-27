import pandas as pd

df = pd.read_csv('shopping_data_missingvalue.csv')

print("Data sebelum pre-processing")
print(df)

missing_value = df.isnull().sum()
print("Jumlah missing value per kolom :")
print(missing_value)

df_clean = df.dropna()
print("Data setelah menghapus baris yang mengandung missing value :")
print(df_clean)

df_mean = df.fillna(df.mean(numeric_only=True))
print("Data setelah mengisi missing value dengan mean :")
print(df_mean)

df_median = df.fillna(df.median(numeric_only=True))
print("Data setelah mengisi missing value dengan median :")
print(df_median)