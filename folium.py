import folium
clcoding = folium .Map(
    location = [17.7, 84.9],
    zoom_start =6,
    tiles = "OpenStreetMap"
)

folium.Marker(
    locatin = [17.7, 84.9],
    tooltip = "Cyclon Akvan",
    popup = "IMD position : 20 NOV 02:30 IST",
    icon = folium.Icon(color = "blue", icon = "cloud")
).add_to(clcoding)

clcoding