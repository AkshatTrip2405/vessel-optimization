import folium

def create_route_map():

    route = [
        [29.95, -90.07],   # New Orleans
        [20.00, -60.00],   # Waypoint 1
        [10.00, 20.00],    # Waypoint 2
        [1.29, 103.85]     # Singapore
    ]

    m = folium.Map(
        location=[15, 20],
        zoom_start=2
    )

    folium.PolyLine(
        route,
        weight=5
    ).add_to(m)

    folium.Marker(
        route[0],
        popup="New Orleans"
    ).add_to(m)

    folium.Marker(
        route[-1],
        popup="Singapore"
    ).add_to(m)

    folium.Marker(
        route[1],
        popup="""
        Wind: 25 kn
        Wave: 4.5 m
        Speed Loss: 0.7 kn
        """
    ).add_to(m)

    folium.Marker(
        route[2],
        popup="""
        Wind: 12 kn
        Wave: 2.0 m
        Speed Loss: 0.2 kn
        """
    ).add_to(m)

    m.save("templates/route_map.html")