# brent-oil-bayesian-change-point-analysis_week_11
Bayesian change point analysis of Brent oil prices to quantify the impact of major geopolitical, economic, and OPEC-related events using PyMC and time series methods.
## Project Overview

This project applies Bayesian Change Point Analysis to historical Brent oil prices (1987–2022) to identify structural breaks in price behavior and associate them with major geopolitical, economic, and OPEC-related events.

The analysis supports data-driven decision-making for investors, policymakers, and energy companies by quantifying how significant global events influence oil price dynamics under uncertainty.

Key techniques include:
- Time series exploratory analysis
- Log-return transformation and stationarity testing
- Bayesian inference using PyMC
- Probabilistic change point detection
- Event-based interpretation of market regime shifts
## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/your-username/brent-oil-bayesian-change-point-analysis.git
cd brent-oil-bayesian-change-point-analysis
### 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
### 3. Install Dependencies
pip install -r requirements.txt
### 4. Data Location

Place the following files in the data/ directory:
BrentOilPrices.csv
key_oil_market_events.csv
Key events are loaded from data/key_oil_market_events.csv and used to contextualize volatility spikes and detected change points.
Methodology

Time series exploratory analysis of raw prices

Log-return transformation for stationarity

Augmented Dickey-Fuller (ADF) testing

Volatility analysis using rolling statistics

Bayesian reasoning to motivate change point detection

Assumptions & Limitations

Change points identify statistical associations, not causal proof

Multiple overlapping events may influence price shifts

Market reactions may precede or lag event dates

External drivers (FX, demand, speculation) are not explicitly modeled

Communication of Results

Investors: dashboards and summary reports highlighting regime shifts

Policymakers: analytical reports supporting energy security decisions

Energy companies: insights on volatility, risk, and operational planning

Tools

Python 3.11, Pandas, NumPy, Matplotlib, Statsmodels, PyMC, ArviZ, Jupyter