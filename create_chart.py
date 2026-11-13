
import pandas as pd
import matplotlib.pyplot as plt

# Load analysis results
df = pd.read_csv("step_completion_analysis.csv")

# Prepare chart data
groups = df["step_group"]
rates = df["shortlist_rate_pct"]
counts = df["applications"]

# Create bar chart
plt.figure(figsize=(9, 6))

bars = plt.bar(groups, rates)

# Add percentage and application count labels
for bar, rate, count in zip(bars, rates, counts):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1,
        f"{rate:.1f}%\n(n={count})",
        ha="center",
        fontsize=11
    )

# Chart formatting
plt.title(
    "Shortlist Rate by Application Step Completion",
    fontsize=14
)
plt.xlabel("Application Completion Group")
plt.ylabel("Shortlist Rate (%)")
plt.ylim(0, 60)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()

# Save chart
plt.savefig(
    "shortlist_rate_by_steps.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Chart saved successfully!")
