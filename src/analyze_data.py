
import pandas as pd

# Load original dataset
df = pd.read_csv("data/raw/OSM_four_arc_merged_V3.csv")

print("===== GEOPULSE CATEGORY CLEANING =====")

# Normalize category text
df["Category_Clean"] = (
    df["Category"]
    .str.strip()
    .str.casefold()
)

# Category counts after normalization
category_summary = (
    df["Category_Clean"]
    .value_counts()
    .reset_index()
)

category_summary.columns = ["Category", "Venue_Count"]

# Display top 15 categories
print("\nTop 15 Categories After Cleaning:")
print(category_summary.head(15).to_string(index=False))

# Save category summary
category_summary.to_csv(
    "reports/category_summary.csv",
    index=False
)

print("\nOriginal Categories:", df["Category"].nunique())
print("Cleaned Categories:", df["Category_Clean"].nunique())

print("\nCategory summary saved successfully!")
print("Location: reports/category_summary.csv")
