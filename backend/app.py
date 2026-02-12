from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import json
import os

app = Flask(__name__)
CORS(app)

# Get absolute path to backend/data folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data")


# -----------------------------
# Prices API
# -----------------------------
@app.route("/api/prices")
@app.route("/api/prices")
def get_prices():
    df = pd.read_csv(os.path.join(DATA_PATH, "BrentOilPrices.csv"))

    # Rename columns to standard format
    df.columns = df.columns.str.strip()
    df.rename(columns={"Date": "date", "Price": "price"}, inplace=True)

    df["date"] = pd.to_datetime(df["date"])

    return jsonify(df.to_dict(orient="records"))



# -----------------------------
# Events API
# -----------------------------
@app.route("/api/events")
def get_events():
    df = pd.read_csv(os.path.join(DATA_PATH, "key_oil_market_events.csv"))

    df.columns = df.columns.str.strip()
    df.rename(columns={"Date": "date"}, inplace=True)

    df["date"] = pd.to_datetime(df["date"])

    return jsonify(df.to_dict(orient="records"))



# -----------------------------
# Change Point API
# -----------------------------
@app.route("/api/change-points")
def get_change_points():
    with open(os.path.join(DATA_PATH, "change_point_results.json")) as f:
        results = json.load(f)
    return jsonify(results)


# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Brent Oil Analysis API is running",
        "endpoints": [
            "/api/prices",
            "/api/events",
            "/api/change-points"
        ]
    })


if __name__ == "__main__":
    app.run(debug=True)
