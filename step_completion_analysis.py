


import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_applications.csv")

# Group applicants by completed steps
df["step_group"] = df["steps_done"].apply(
    lambda x: "All 4 steps" if x == 4 else "Fewer than 4"
)

# Calculate applications and shortlisted applicants
step_analysis = df.groupby("step_group").agg(
    applications=("application_id", "count"),
    shortlisted=("shortlisted", lambda x: (x == "yes").sum())
).reset_index()

# Calculate shortlist percentage
step_analysis["shortlist_rate_pct"] = (
    step_analysis["shortlisted"] /
    step_analysis["applications"]
) * 100

# Display results
print("\n===== SHORTLIST RATE BY STEP COMPLETION =====")
print(step_analysis.round(2).to_string(index=False))

# Calculate percentage-point difference
rates = step_analysis.set_index("step_group")["shortlist_rate_pct"]

gap = rates["All 4 steps"] - rates["Fewer than 4"]

print(f"\nShortlist rate difference: {gap:.2f} percentage points")

# Save result
step_analysis.to_csv("step_completion_analysis.csv", index=False)

print("\nStep completion analysis saved successfully!")
