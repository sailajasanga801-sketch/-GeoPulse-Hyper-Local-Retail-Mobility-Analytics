
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

DATA_PATH = "data/raw/OSM_four_arc_merged_V3.csv"


def load_data():
    df = pd.read_csv(DATA_PATH)

    df["Category_Clean"] = (
        df["Category"]
        .astype(str)
        .str.strip()
        .str.casefold()
    )

    return df


@app.route("/")
def home():

    df = load_data()

    # Category dropdown options
    categories = sorted(
        df["Category_Clean"].dropna().unique()
    )

    # Selected category
    selected_category = request.args.get(
        "category", "all"
    )

    # Filter dataset
    if selected_category != "all":
        filtered_df = df[
            df["Category_Clean"] == selected_category
        ]
    else:
        filtered_df = df

    # Dashboard metrics
    total_venues = len(filtered_df)
    total_categories = df["Category_Clean"].nunique()

    top_category = (
        df["Category_Clean"].value_counts().idxmax()
    )

    # Top 10 category chart
    top_categories = (
        df["Category_Clean"]
        .value_counts()
        .head(10)
        .to_dict()
    )

    # Venue details table
    venue_records = (
        filtered_df[
            [
                "Venue",
                "Category_Clean",
                "Venue Latitude",
                "Venue Longitude"
            ]
        ]
        .head(100)
        .to_dict(orient="records")
    )

    return render_template(
        "index.html",
        total_venues=total_venues,
        total_categories=total_categories,
        top_category=top_category.title(),
        top_categories=top_categories,
        categories=categories,
        selected_category=selected_category,
        venue_records=venue_records
    )


if __name__ == "__main__":
    app.run(debug=True)
