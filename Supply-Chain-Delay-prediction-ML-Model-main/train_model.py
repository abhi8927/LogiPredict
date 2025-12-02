import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("shipment_data.csv")
categorical = ["vehicle_type", "weather"]  # remove 'carrier'


# Features and target
X = df.drop("delay_days", axis=1)
y = df["delay_days"]

# Define feature types
categorical = ["vehicle_type", "weather", "carrier"]
numerical = ["distance_km", "vendor_rating"]

# Preprocessing pipeline
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
], remainder="passthrough")

# Full pipeline with RandomForest
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train-test split for better evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)

# Evaluate
train_preds = model.predict(X_train)
test_preds = model.predict(X_test)

print("📊 Model Performance:")
print(f"→ Train MAE: {mean_absolute_error(y_train, train_preds):.2f}")
print(f"→ Test  MAE: {mean_absolute_error(y_test, test_preds):.2f}")
print(f"→ Test  R² Score: {r2_score(y_test, test_preds):.2f}")

# Save model
joblib.dump(model, "delay_predictor_model.pkl")
print("Model saved as delay_predictor_model.pkl")
