
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_applications.csv")

print("DATASET LOADED:", df.shape)

# Calculate applications by source
source_analysis = df.groupby("source").agg(
    total_applications=("application_id", "count"),
    total_hires=("hired", lambda x: (x == "yes").sum())
)

# Calculate hires per 100 applications
source_analysis["hires_per_100"] = (
    source_analysis["total_hires"]
    / source_analysis["total_applications"]
) * 100

# Sort from highest to lowest
source_analysis = source_analysis.sort_values(
    by="hires_per_100",
    ascending=False
)

print("\n===== SOURCE PERFORMANCE =====")
print(source_analysis.round(2))

# Identify the best source
best_source = source_analysis.index[0]

print("\n===== BEST APPLICATION SOURCE =====")
print("Best Source:", best_source)

print(
    "Hires per 100 applications:",
    round(source_analysis.loc[best_source, "hires_per_100"], 2)
)

# Save results
source_analysis.to_csv("source_analysis.csv")

print("\nSource analysis saved successfully!")
