from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def generate_pdf(data):

    if not os.path.exists("generated_reports"):
        os.makedirs("generated_reports")

    filename = "generated_reports/vessel_report.pdf"

    c = canvas.Canvas(filename, pagesize=letter)

    width, height = letter

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, 760, "VESSEL PERFORMANCE REPORT")

    y = 720

    # ==========================
    # Vessel Details
    # ==========================

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "VESSEL INFORMATION")
    y -= 25

    c.setFont("Helvetica", 12)

    c.drawString(60, y, f"Vessel Name: {data['vessel_name']}")
    y -= 20

    c.drawString(60, y, f"Voyage Number: {data['voyage_number']}")
    y -= 35

    # ==========================
    # Performance Analysis
    # ==========================

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "PERFORMANCE ANALYSIS")
    y -= 25

    c.setFont("Helvetica", 12)

    c.drawString(60, y, f"Speed Variance: {data['speed_variance']} Knots")
    y -= 20

    c.drawString(60, y, f"Fuel Variance: {data['fuel_variance']} MT/day")
    y -= 20

    c.drawString(60, y, f"Extra Fuel Cost: ${data['extra_fuel_cost']}")
    y -= 20

    c.drawString(60, y, f"Status: {data['status']}")
    y -= 35

    # ==========================
    # Weather Analysis
    # ==========================

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "WEATHER ANALYSIS")
    y -= 25

    c.setFont("Helvetica", 12)

    c.drawString(60, y, f"Weather Risk: {data['weather_risk']}")
    y -= 20

    c.drawString(
        60,
        y,
        f"Estimated Speed Loss: {data['estimated_speed_loss']} Knots"
    )
    y -= 35

    # ==========================
    # Voyage Optimization
    # ==========================

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "VOYAGE OPTIMIZATION")
    y -= 25

    c.setFont("Helvetica", 12)

    c.drawString(
        60,
        y,
        f"Original Voyage Time: {data['voyage_time']} Hours"
    )
    y -= 20

    c.drawString(
        60,
        y,
        f"Optimized Voyage Time: {data['optimized_voyage_time']} Hours"
    )
    y -= 20

    c.drawString(
        60,
        y,
        f"Optimized Speed: {data['optimized_speed']} Knots"
    )
    y -= 35

    # ==========================
    # Recommendation
    # ==========================

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "RECOMMENDATION")
    y -= 25

    c.setFont("Helvetica", 12)

    if data["weather_risk"] == "HIGH":
        recommendation = "Consider Alternate Route"
    elif data["weather_risk"] == "MEDIUM":
        recommendation = "Monitor Weather Closely"
    else:
        recommendation = "Proceed With Current Route"

    c.drawString(60, y, recommendation)
    y -= 25

    c.save()

    return filename