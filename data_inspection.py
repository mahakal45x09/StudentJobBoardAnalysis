
import pandas as pd

# Load dataset
df = pd.read_csv("job-board-applications.csv")

print("=" * 50)
print("1. DATASET INFORMATION")
print("=" * 50)

print("Rows and Columns:", df.shape)

print("\nColumn Information:")
df.info()

print("\n" + "=" * 50)
print("2. MISSING VALUES")
print("=" * 50)

print(df.isnull().sum())

print("\n" + "=" * 50)
print("3. DUPLICATE RECORDS")
print("=" * 50)

print("Duplicate rows:", df.duplicated().sum())

print("Duplicate Application IDs:",
      df["application_id"].duplicated().sum())

print("\n" + "=" * 50)
print("4. UNIQUE CATEGORY VALUES")
print("=" * 50)

for col in ["role_category", "work_mode", "source",
            "shortlisted", "interviewed", "hired"]:

    print(f"\n{col}:")
    print(df[col].value_counts(dropna=False))

print("\n" + "=" * 50)
print("5. NUMERIC DATA SUMMARY")
print("=" * 50)

print(df[[
    "stipend_inr_month",
    "steps_done",
    "days_to_first_reply"
]].describe())

print("\n" + "=" * 50)
print("6. DATE RANGE")
print("=" * 50)

df["applied_on"] = pd.to_datetime(
    df["applied_on"], errors="coerce"
)

print("Starting Date:", df["applied_on"].min())
print("Ending Date:", df["applied_on"].max())

print("\nDATA INSPECTION COMPLETED!")
