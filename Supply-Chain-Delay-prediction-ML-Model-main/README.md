# PredictNTrack: Shipment Delay Predictor & Optimizer

PredictNTrack is an intelligent machine learning-powered web application built using Flask that predicts potential shipment delays and suggests optimal shipment actions like mode-switching or route changes. It helps logistics teams minimize disruption by making data-driven shipping decisions.

---

## Features

- Predict shipment delay (in days) using machine learning
- Considers factors like distance, weather, vehicle type, carrier, and vendor rating
- ML-based suggestions for:
  - Switching to alternate modes (e.g., rail if road delay is high)
  - Re-routing through less-affected highways
- Download shipment reports as PDF/CSV
- Trained on synthetic + realistic shipment data

---

## ML Model

- Algorithm: Random Forest Regressor
- Inputs:
  - `distance_km`
  - `weather` (e.g., Clear, Rain, Fog)
  - `vehicle_type` (e.g., Truck, Train)
  - `vendor_rating` (1-5)
  - `carrier` (FedEx, BlueDart, etc.)
- Output: Delay in days (float)
- Trained with Scikit-learn pipeline + OneHotEncoder for categorical features

---

## Project Structure

predictntrack_project/
├── app.py # Flask web app
├── model_training.py # ML model training script
├── delay_predictor_model.pkl
├── shipment_data.csv # Sample data for training
├── templates/
│ └── index.html
├── static/
│ └── style.css
├── requirements.txt
└── README.md

App will be live on: http://127.0.0.1:5000
