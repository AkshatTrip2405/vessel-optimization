import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_charts():

    if not os.path.exists("static"):
        os.makedirs("static")

    try:
        df = pd.read_csv("data/voyage_history.csv")

        # Fuel Cost Chart
        plt.figure(figsize=(8,4))
        plt.plot(df["Extra Fuel Cost"], marker="o")
        plt.title("Extra Fuel Cost Trend")
        plt.xlabel("Voyage Number")
        plt.ylabel("Cost ($)")
        plt.tight_layout()
        plt.savefig("static/fuel_cost_chart.png")
        plt.close()

        # Weather Risk Chart
        plt.figure(figsize=(6,6))
        df["Weather Risk"].value_counts().plot(kind="pie", autopct="%1.1f%%")
        plt.ylabel("")
        plt.title("Weather Risk Distribution")
        plt.tight_layout()
        plt.savefig("static/weather_chart.png")
        plt.close()

    except Exception as e:
        print("Chart Error:", e)