
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_applications.csv")

# Classify applications
df["paid_status"] = df["stipend_inr_month"].apply(
    lambda x: "Paid" if x > 0 else "Unpaid"
)

# Identify recorded replies
df["reply_received"] = df["days_to_first_reply"].notna()

# Group and calculate metrics
paid_analysis = df.groupby("paid_status").agg(
    applications=("application_id", "count"),
    replied=("reply_received", "sum"),
    mean_reply_days=("days_to_first_reply", "mean"),
    median_reply_days=("days_to_first_reply", "median")
).reset_index()

# Calculate no-reply count and percentage
paid_analysis["no_reply"] = (
    paid_analysis["applications"] - paid_analysis["replied"]
)

paid_analysis["no_reply_pct"] = (
    paid_analysis["no_reply"] /
    paid_analysis["applications"]
) * 100

# Display results
print("\n===== PAID VS UNPAID RESPONSE ANALYSIS =====")
print(paid_analysis.round(2).to_string(index=False))

# Save results
paid_analysis.to_csv("paid_unpaid_analysis.csv", index=False)

print("\nPaid vs unpaid analysis saved successfully!")
