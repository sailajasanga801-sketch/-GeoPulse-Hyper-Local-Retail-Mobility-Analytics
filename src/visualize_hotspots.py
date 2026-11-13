
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw/OSM_four_arc_merged_V3.csv")

# Create geographic density visualization
plt.figure(figsize=(12, 8))

plt.hexbin(
    df["Venue Longitude"],
    df["Venue Latitude"],
    gridsize=35,
    cmap="YlOrRd",
    mincnt=1
)

# Add color bar
plt.colorbar(label="Number of Venues")

# Chart details
plt.title("Geographic Venue Density - Mumbai", fontsize=16)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(alpha=0.2)

plt.tight_layout()

# Save visualization
plt.savefig(
    "reports/mumbai_venue_density.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Geographic hotspot visualization saved successfully!")
