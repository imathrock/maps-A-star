import osmnx as ox

def display_graph(filename):
    graph = ox.load_graphml(str(filename))
    ox.plot_graph(graph)

if __name__ == "__main__":
    file = input("File Name:")
    display_graph(file)