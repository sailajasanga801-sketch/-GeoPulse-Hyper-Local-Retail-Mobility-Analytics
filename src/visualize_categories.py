
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw/OSM_four_arc_merged_V3.csv")

# Clean category names
df["Category_Clean"] = (
    df["Category"].str.strip().str.casefold()
)

# Calculate top 10 categories
top_categories = df["Category_Clean"].value_counts().head(10)

# Create bar chart
plt.figure(figsize=(12, 7))

top_categories.sort_values().plot(
    kind="barh",
    edgecolor="black"
)

plt.title("Top 10 Venue Categories in Mumbai", fontsize=16)
plt.xlabel("Number of Venues")
plt.ylabel("Category")
plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.tight_layout()

# Save chart
plt.savefig(
    "reports/top_10_categories.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Category visualization saved successfully!")
