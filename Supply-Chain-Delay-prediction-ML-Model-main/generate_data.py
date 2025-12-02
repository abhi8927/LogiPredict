import pandas as pd
import random

def generate_data(num_samples=500):
    data = []
    for _ in range(num_samples):
        distance_km = random.randint(50, 2000)
        vehicle_type = random.choice(['Truck', 'Van', 'Bike'])
        vendor_rating = random.randint(1, 5)
        weather = random.choice(['Sunny', 'Rain', 'Storm', 'Fog'])

        # Delay logic (more realistic)
        base_delay = distance_km / 800
        if weather == 'Storm':
            base_delay += 2
        elif weather == 'Rain':
            base_delay += 1
        elif weather == 'Fog':
            base_delay += 1.5

        if vehicle_type == 'Bike':
            base_delay += 0.5
        elif vehicle_type == 'Truck':
            base_delay += 1

        base_delay += (5 - vendor_rating) * 0.3

        delay_days = round(base_delay + random.uniform(-0.5, 0.5), 2)
        delay_days = max(0, delay_days)

        data.append([distance_km, vehicle_type, vendor_rating, weather, delay_days])

    df = pd.DataFrame(data, columns=["distance_km", "vehicle_type", "vendor_rating", "weather", "delay_days"])
    df.to_csv("shipment_data.csv", index=False)
    print(" Synthetic data saved to shipment_data.csv")

if __name__ == "__main__":
    generate_data()
