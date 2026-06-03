import csv
import os
from datetime import datetime

FILE_NAME = "data/voyage_history.csv"

def save_voyage(report):

    if not os.path.exists("data"):
        os.makedirs("data")

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Vessel",
                "Voyage",
                "Speed Variance",
                "Fuel Variance",
                "Weather Risk",
                "Extra Fuel Cost",
                "Status"
            ])

        writer.writerow([
            datetime.now().strftime("%d-%m-%Y %H:%M"),
            report["vessel_name"],
            report["voyage_number"],
            report["speed_variance"],
            report["fuel_variance"],
            report["weather_risk"],
            report["extra_fuel_cost"],
            report["status"]
        ])