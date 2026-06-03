# Vessel Performance & Voyage Optimization System

## Overview

The Vessel Performance & Voyage Optimization System is a Flask-based web application designed to analyze vessel performance, evaluate voyage efficiency, assess weather impacts, generate optimization recommendations, and maintain historical voyage records.

The system helps shipping operators monitor vessel performance, estimate fuel costs, analyze weather-related risks, and identify opportunities for voyage optimization.

---

## Features

### Vessel Performance Analysis

* Speed variance calculation
* Fuel consumption variance analysis
* Extra fuel cost estimation
* Vessel performance status evaluation

### Weather Risk Assessment

* Wind speed analysis
* Wave height analysis
* Weather risk classification (LOW / MEDIUM / HIGH)
* Estimated speed loss calculation

### Voyage Optimization

* Voyage duration calculation
* Optimized speed recommendation
* Fuel requirement estimation
* Alternative route suggestion
* Cost-saving analysis

### Reporting

* Detailed PDF report generation
* Downloadable vessel performance reports

### Route Visualization

* Interactive voyage route map using Folium and OpenStreetMap

### Historical Analytics

* Voyage history storage in CSV format
* Historical dashboard
* Weather risk distribution chart
* Fuel cost trend analysis
* Statistical summaries

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* Pandas
* Matplotlib
* ReportLab
* Folium
* OpenStreetMap

---

## Project Structure

```text
vessel-optimization/
│
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── modules/
│   ├── report_generator.py
│   ├── voyage_calculator.py
│   ├── route_map.py
│   ├── history_manager.py
│   ├── dashboard.py
│   └── chart_generator.py
│
├── templates/
│   ├── index.html
│   └── route_map.html
│
├── static/
│   ├── style.css
│   ├── fuel_cost_chart.png
│   └── weather_chart.png
│
├── data/
│   └── voyage_history.csv
│
└── generated_reports/
    └── vessel_report.pdf
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/vessel-optimization.git
cd vessel-optimization
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Sample Input

### Vessel Information

* Vessel Name: MV Dehradun
* Voyage Number: V001

### Benchmark Data

* Benchmark Speed: 13 knots
* Benchmark Fuel: 30 MT/day
* Fuel Price: 650 USD/MT

### Noon Report

* Actual Speed: 12 knots
* Actual Fuel Consumption: 32 MT/day

### Weather Data

* Wind Speed: 10 knots
* Wave Height: 0.8 meters

### Voyage Optimization

* Distance: 5000 NM
* STW Speed: 12 knots

---

## Outputs

The application generates:

* Vessel Performance Report
* Voyage Optimization Report
* Interactive Route Map
* PDF Report
* Historical Dashboard
* Weather Risk Analytics
* Fuel Cost Trend Charts

---

## Future Enhancements

* Real-time weather API integration
* AIS vessel tracking integration
* Machine Learning-based fuel prediction
* Multi-vessel fleet management
* Database integration (MySQL/PostgreSQL)
* User authentication and role management

---

## Author

Akshat Tripathi

B.Tech Computer Science & Engineering

Graphic Era University
