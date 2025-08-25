import osmnx as ox

def download_osm(city_name, file_name="osm_data.graphml"):
    graph = ox.graph_from_place(city_name, network_type="drive")
    ox.save_graphml(graph, file_name)
    print(f"Saved OSM data for {city_name} to {file_name}")


if __name__ == "__main__":
    city = input("Enter city name (e.g., 'Paris, France'): ")
    download_osm(city, f"{city.replace(',', '').replace(' ', '_')}.graphml")
