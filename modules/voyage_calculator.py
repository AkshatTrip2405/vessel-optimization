def calculate_voyage(
    distance,
    speed,
    daily_consumption,
    fuel_price,
    weather_risk
):

    voyage_days = distance / (speed * 24)

    fuel_required = voyage_days * daily_consumption

    total_cost = fuel_required * fuel_price

    if weather_risk == "HIGH":
        alt_distance = distance * 1.05
        alt_fuel = fuel_required * 0.90

    elif weather_risk == "MEDIUM":
        alt_distance = distance * 1.03
        alt_fuel = fuel_required * 0.95

    else:
        alt_distance = distance
        alt_fuel = fuel_required

    alt_days = alt_distance / (speed * 24)

    alt_cost = alt_fuel * fuel_price

    fuel_saved = fuel_required - alt_fuel

    money_saved = total_cost - alt_cost

    return {
        "voyage_days": round(voyage_days, 2),
        "fuel_required": round(fuel_required, 2),
        "total_cost": round(total_cost, 2),
        "alt_distance": round(alt_distance, 2),
        "alt_days": round(alt_days, 2),
        "alt_fuel": round(alt_fuel, 2),
        "alt_cost": round(alt_cost, 2),
        "fuel_saved": round(fuel_saved, 2),
        "money_saved": round(money_saved, 2)
    }