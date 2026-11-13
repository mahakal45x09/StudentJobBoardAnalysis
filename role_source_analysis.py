
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_applications.csv")

# Group by role and source
role_analysis = df.groupby(
    ["role_category", "source"]
).agg(
    total_applications=("application_id", "count"),
    total_hires=("hired", lambda x: (x == "yes").sum())
).reset_index()

# Calculate hires per 100 applications
role_analysis["hires_per_100"] = (
    role_analysis["total_hires"]
    / role_analysis["total_applications"]
) * 100

# Display complete results
print("\n===== ROLE-WISE SOURCE PERFORMANCE =====")

print(role_analysis.round(2).to_string(index=False))

# Find best source within each role
best_sources = role_analysis.loc[
    role_analysis.groupby("role_category")[
        "hires_per_100"
    ].idxmax()
]

print("\n===== BEST SOURCE FOR EACH ROLE =====")

print(
    best_sources[
        ["role_category", "source",
         "total_applications", "total_hires",
         "hires_per_100"]
    ].round(2).to_string(index=False)
)

# Save results
role_analysis.to_csv(
    "role_source_analysis.csv",
    index=False
)

best_sources.to_csv(
    "best_source_by_role.csv",
    index=False
)

print("\nRole-wise analysis saved successfully!")
