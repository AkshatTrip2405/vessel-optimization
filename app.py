from flask import Flask, render_template, request
from flask import send_file
from modules.report_generator import generate_pdf
from modules.voyage_calculator import calculate_voyage
from modules.route_map import create_route_map
from modules.history_manager import save_voyage
from modules.dashboard import get_dashboard_data
from modules.chart_generator import generate_charts

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    report = None
    voyage_data = None

    if request.method == "POST":

        vessel_name = request.form.get("vessel_name", "")
        voyage_number = request.form.get("voyage_number", "")

        benchmark_speed = float(request.form.get("benchmark_speed", 0))
        benchmark_fuel = float(request.form.get("benchmark_fuel", 0))
        fuel_price = float(request.form.get("fuel_price", 0))

        actual_speed = float(request.form.get("actual_speed", 0))
        actual_fuel = float(request.form.get("actual_fuel", 0))

        wind_speed = float(request.form.get("wind_speed", 0))
        wave_height = float(request.form.get("wave_height", 0))

        distance = float(request.form.get("distance", 0))
        stw_speed = float(request.form.get("stw_speed", 1))

        speed_variance = round(
            actual_speed - benchmark_speed,
            2
        )

        fuel_variance = round(
            actual_fuel - benchmark_fuel,
            2
        )

        extra_fuel_cost = round(
            max(0, fuel_variance * fuel_price),
            2
        )

        weather_risk = "LOW"

        if wind_speed > 25 or wave_height > 4:
            weather_risk = "HIGH"

        elif wind_speed > 15 or wave_height > 2:
            weather_risk = "MEDIUM"

        estimated_speed_loss = round(
            wave_height * 0.5,
            2
        )

        optimized_speed = round(
            max(stw_speed - estimated_speed_loss, 1),
            2
        )

        voyage_time = round(
            distance / stw_speed,
            2
        ) if stw_speed > 0 else 0

        optimized_voyage_time = round(
            distance / optimized_speed,
            2
        )

        status = "Within Limits"

        if speed_variance < 0 or fuel_variance > 0:
            status = "Under Performance"

        report = {
            "vessel_name": vessel_name,
            "voyage_number": voyage_number,

            "speed_variance": speed_variance,
            "fuel_variance": fuel_variance,
            "extra_fuel_cost": extra_fuel_cost,

            "weather_risk": weather_risk,
            "estimated_speed_loss": estimated_speed_loss,

            "optimized_speed": optimized_speed,
            "voyage_time": voyage_time,
            "optimized_voyage_time": optimized_voyage_time,

            "status": status
        }

        voyage_data = calculate_voyage(
            distance,
            stw_speed,
            benchmark_fuel,
            fuel_price,
            weather_risk
        )

        # Generate Route Map
        create_route_map()

        # Generate PDF
        save_voyage(report)
        generate_charts()

        pdf_path = generate_pdf(report)

        report["pdf_path"] = pdf_path

    dashboard = get_dashboard_data()

    return render_template(
        "index.html",
        report=report,
        voyage_data=voyage_data,
        dashboard=dashboard
        )


@app.route("/route_map")
def route_map():
    return render_template("route_map.html")

@app.route("/download_report")
def download_report():
    return send_file(
        "generated_reports/vessel_report.pdf",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)