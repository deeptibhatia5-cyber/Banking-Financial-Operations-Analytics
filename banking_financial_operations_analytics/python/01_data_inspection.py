from pathlib import Path
import pandas as pd

# Place the downloaded CSV in data/raw and update the filename below.
DATA_PATH = Path("../data/raw/transactions.csv")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_PATH.resolve()}\n"
        "Download a suitable public CSV dataset and place it in data/raw/."
    )

df = pd.read_csv(DATA_PATH)

print("\nFirst 10 rows")
print(df.head(10))

print("\nLast 5 rows")
print(df.tail(5))

print("\nShape (rows, columns)")
print(df.shape)

print("\nColumn names")
print(df.columns.tolist())

print("\nData types")
print(df.dtypes)

print("\nMissing values")
print(df.isna().sum())

print("\nDuplicate rows")
print(df.duplicated().sum())

# Once the actual column names are confirmed, add project-specific
# validation for transaction IDs, dates, amounts, and statuses.
