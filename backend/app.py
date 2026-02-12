from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

DATA_PATH = "data/"


@app.route("/api/prices")
def get_prices():
    df = pd.read_csv(DATA_PATH + "brent_prices.csv")
    df["date"] = pd.to_datetime(df["date"])
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/events")
def get_events():
    df = pd.read_csv(DATA_PATH + "key_oil_market_events.csv")
    df["date"] = pd.to_datetime(df["date"])
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/change-points")
def get_change_points():
    with open(DATA_PATH + "change_point_results.json") as f:
        results = json.load(f)
    return jsonify(results)
@app.route("/")
def home():
    return {
        "message": "Brent Oil Analysis API is running",
        "endpoints": [
            "/api/prices",
            "/api/events",
            "/api/change-points"
        ]
    }


if __name__ == "__main__":
    app.run(debug=True)
