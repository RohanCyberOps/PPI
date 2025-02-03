import folium

# Create a map object centered at a specific location (latitude, longitude)
map_center = [28.6139, 77.2090]  # Example coordinates for Delhi, India
my_map = folium.Map(location=map_center, zoom_start=12)

# Add a marker
folium.Marker(location=[28.6139, 77.2090], popup="Delhi Center").add_to(my_map)

# Add a circle marker
folium.CircleMarker(
    location=[28.7041, 77.1025],  # Example coordinates for another location
    radius=10,
    popup="Another Location",
    color="blue",
    fill=True,
    fill_color="cyan",
).add_to(my_map)

# Save the map to an HTML file
my_map.save("map.html")

print("Map generated! Open 'map.html' to view.")
