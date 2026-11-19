
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load Mumbai POI dataset
DATA_PATH = "data/raw/OSM_four_arc_merged_V3.csv"


def load_data():
    df = pd.read_csv(DATA_PATH)

    df["Category_Clean"] = (
        df["Category"].astype(str).str.strip().str.casefold()
    )

    return df


@app.route("/")
def home():
    df = load_data()

    total_venues = len(df)
    total_categories = df["Category_Clean"].nunique()

    top_category = (
        df["Category_Clean"].value_counts().idxmax()
    )

    top_categories = (
        df["Category_Clean"]
        .value_counts()
        .head(10)
        .to_dict()
    )

    return render_template(
        "index.html",
        total_venues=total_venues,
        total_categories=total_categories,
        top_category=top_category.title(),
        top_categories=top_categories
    )


if __name__ == "__main__":
    app.run(debug=True)
