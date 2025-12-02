import joblib
import pandas as pd

# Load trained model
model = joblib.load("delay_predictor_model.pkl")

def predict_delay(shipment_input=None):
    if shipment_input is None:
        shipment_input = {
            "distance_km": 450,
            "weather": "Rain",
            "vehicle_type": "Truck",
            "vendor_rating": 3,
            "carrier": "Delhivery"   # ✅ REQUIRED NOW
        }

    # Convert to DataFrame
    input_df = pd.DataFrame([shipment_input])
    
    # Predict
    predicted_delay = model.predict(input_df)[0]

    # Reasoning logic (can be improved later)
    reason = "Based on past patterns, weather and vendor rating may have caused this delay."

    return {
        "input": shipment_input,
        "predicted_delay_days": round(predicted_delay, 2),
        "reason": reason
    }
