import polars as pl
import datetime

df = pl.read_csv(r"data/drugs_side_effects_drugs_com.csv")

print(df.shape)
print(df.sample(5))
print(df.schema)