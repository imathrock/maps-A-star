import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_node("B")
G.add_node("C")


G.add_edge("A", "B")
G.add_edge("B", "C")

nx.write_graphml(G, "my_graph.graphml")

print("GraphML file created: my_graph.graphml")

nx.draw(G, with_labels=True, node_size=800, node_color="lightblue", font_size=10)
plt.show()

