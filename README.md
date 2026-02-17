# Brent Oil Bayesian Change Point Analysis

## 📌 Project Overview

This project analyzes historical Brent Oil prices to detect structural changes using Bayesian Change Point Detection. The goal is to identify significant market shifts and relate them to major global oil market events.

The project is divided into three main tasks:

- Task 1: Exploratory Data Analysis (EDA) & Interim Report
- Task 2: Bayesian Change Point Modeling
- Task 3: Full-Stack Dashboard (Flask + React)

---

# 🧠 Task 1: Exploratory Data Analysis (EDA)

## Objective
Understand the structure, distribution, and trends of Brent oil prices.

## Steps Performed
- Loaded and cleaned BrentOilPrices.csv
- Converted Date column to datetime
- Visualized price trends over time
- Summary statistics analysis
- Identified volatility patterns

## Output
- Clean dataset
- Initial insights report (Interim Report)
- Visualizations of price movement

---

# 🔬 Task 2: Bayesian Change Point Detection

## Objective
Detect structural breakpoints in Brent oil prices using Bayesian methods.

## Approach
- Modeled price time series
- Applied Bayesian change point detection
- Identified probable regime shifts
- Saved detected change points

## Output
- change_point_results.json
- Interpretation of major change periods

---

# 🌐 Task 3: Full-Stack Dashboard

## Architecture

Frontend:
- React (Vite)
- Chart.js
- Fetch API

Backend:
- Flask
- Pandas
- REST API endpoints

## API Endpoints

- `/api/prices`
- `/api/events`
- `/api/change-points`

## Features

- Interactive Brent oil price chart
- Market event listing
- Detected change points display

---

# 🚀 How to Run the Project

## Backend (Flask)

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py

##Frontend (React)

cd frontend
npm install
npm run dev