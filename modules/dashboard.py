import pandas as pd

def get_dashboard_data():

    try:
        df = pd.read_csv("data/voyage_history.csv")

        return {
            "total_voyages": len(df),
            "avg_speed_variance": round(df["Speed Variance"].mean(), 2),
            "avg_fuel_variance": round(df["Fuel Variance"].mean(), 2),
            "total_extra_cost": round(df["Extra Fuel Cost"].sum(), 2),
            "weather_counts": df["Weather Risk"].value_counts().to_dict()
        }

    except Exception as e:
        print("Dashboard Error:", e)
        return None