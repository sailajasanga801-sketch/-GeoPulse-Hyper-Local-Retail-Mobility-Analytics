
import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/OSM_four_arc_merged_V3.csv")

print("===== GEOPULSE LOCATION HOTSPOT ANALYSIS =====")

# Round coordinates to group nearby venues
df["Latitude_Grid"] = df["Venue Latitude"].round(2)
df["Longitude_Grid"] = df["Venue Longitude"].round(2)

# Count venues in each geographic grid
hotspots = (
    df.groupby(["Latitude_Grid", "Longitude_Grid"])
    .size()
    .reset_index(name="Venue_Count")
    .sort_values("Venue_Count", ascending=False)
)

print("\nTop 15 Location Hotspots:")
print(hotspots.head(15).to_string(index=False))

# Save hotspot analysis
hotspots.to_csv(
    "reports/location_hotspots.csv",
    index=False
)

print("\nTotal Geographic Grids:", len(hotspots))
print("Hotspot analysis saved successfully!")
