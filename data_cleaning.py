
import pandas as pd

# STEP 1: Load original dataset
df = pd.read_csv("job-board-applications.csv")

print("Original dataset shape:", df.shape)

# STEP 2: Remove duplicate application IDs
before = len(df)

df = df.drop_duplicates(
    subset="application_id",
    keep="first"
)

print("\nDuplicates removed:", before - len(df))

# STEP 3: Clean work_mode
df["work_mode"] = (
    df["work_mode"]
    .str.strip()
    .str.lower()
    .replace({"on-site": "on_site"})
)

# STEP 4: Clean source
df["source"] = (
    df["source"]
    .fillna("Unknown")
    .str.strip()
)

df["source"] = df["source"].apply(
    lambda x: "Unknown" if x.lower() == "unknown"
    else x.lower()
)

# STEP 5: Standardize status columns
status_columns = [
    "shortlisted",
    "interviewed",
    "hired"
]

for col in status_columns:
    df[col] = df[col].str.strip().str.lower()

# STEP 6: Convert date into datetime format
df["applied_on"] = pd.to_datetime(
    df["applied_on"],
    errors="coerce"
)

# STEP 7: Check numeric columns
df["stipend_inr_month"] = pd.to_numeric(
    df["stipend_inr_month"],
    errors="coerce"
)

df["steps_done"] = pd.to_numeric(
    df["steps_done"],
    errors="coerce"
)

df["days_to_first_reply"] = pd.to_numeric(
    df["days_to_first_reply"],
    errors="coerce"
)

# STEP 8: Check final dataset
print("\n========== CLEANING REPORT ==========")

print("Final dataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate application IDs:",
      df["application_id"].duplicated().sum())

print("\nWork mode after cleaning:")
print(df["work_mode"].value_counts())

print("\nSources after cleaning:")
print(df["source"].value_counts())

# STEP 9: Save cleaned dataset
df.to_csv("cleaned_applications.csv", index=False)

print("\nCleaned dataset saved successfully!")
