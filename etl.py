import pandas as pd

df = pd.read_csv("input.csv")

df = df.drop_duplicates()

df["salary"] = df["salary"] * 1.10

df.to_csv("output.csv", index=False)

print("ETL Completed")
