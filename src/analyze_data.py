
import pandas as pd

# Load original dataset
df = pd.read_csv("data/raw/OSM_four_arc_merged_V3.csv")

print("===== GEOPULSE CATEGORY ANALYSIS =====")

# Normalize category text
df["Category_Clean"] = (
    df["Category"]
    .str.strip()
    .str.casefold()
)

# Calculate category counts
category_summary = (
    df["Category_Clean"]
    .value_counts()
    .reset_index()
)

category_summary.columns = ["Category", "Venue_Count"]

# Calculate percentage share
total_venues = category_summary["Venue_Count"].sum()

category_summary["Percentage"] = (
    category_summary["Venue_Count"] / total_venues * 100
).round(2)

# Add category rank
category_summary.insert(
    0,
    "Rank",
    range(1, len(category_summary) + 1)
)

# Display top 15 categories
print("\nTop 15 Categories:")
print(category_summary.head(15).to_string(index=False))

# Save updated category summary
category_summary.to_csv(
    "reports/category_summary.csv",
    index=False
)

print("\nTotal Venues:", total_venues)
print("Original Categories:", df["Category"].nunique())
print("Cleaned Categories:", df["Category_Clean"].nunique())

print("\nUpdated category analysis saved successfully!")
print("Location: reports/category_summary.csv")
