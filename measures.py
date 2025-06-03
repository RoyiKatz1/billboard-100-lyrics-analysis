import sys
import networkx as nx
import pandas as pd

# create the variable my_graph
nodes_df = pd.read_csv("first_try_graph/bigram_nodes.csv")
edges_df = pd.read_csv("first_try_graph/bigram_edges.csv")

my_graph = nx.Graph()
my_graph.add_nodes_from(nodes_df['Id'])
my_graph.add_edges_from(edges_df[['source', 'target']].values)

# density calc
density = nx.density(my_graph)
print(f"density: {density:.4f}")

# diameter calc
diameter = nx.diameter(my_graph)
print(f"diameter (Strongly Connected): {diameter}")

#find bridges
bridges = list(nx.bridges(my_graph))
print(f"num of bridges: {len(bridges)}")
for u, v in bridges:
    print(f"bridge: {u} -- {v}")

articulation_points = list(nx.articulation_points(my_graph))

print(f"num of articulation points: {len(articulation_points)}")
for node in articulation_points:
    print(f"critic: {node}")

# betweens calc
# # edge_bc = nx.edge_betweenness_centrality(my_graph, normalized=False)
#
# # nx.edge_betweenness_centrality(my_graph)
#

# try with smaller data
# small_nodes = nodes_df.head(100)
# small_node_ids = set(small_nodes['Id'])


#filter
# small_edges = edges_df[
#     edges_df['source'].isin(small_node_ids) &
#     edges_df['target'].isin(small_node_ids)
# ]


#create
# my_graph = nx.Graph()
# my_graph.add_nodes_from(small_nodes['Id'])
# my_graph.add_edges_from(small_edges[['source', 'target']].values)
# print("graph ready")
#
#
# edge_bc = nx.edge_betweenness_centrality(my_graph)
#
# # הדפיסי תוצאות לדוגמה
# print("noeds:", my_graph.number_of_nodes())
# print("edges:", my_graph.number_of_edges())
# print("top 5 betweenness:")
# for edge, score in sorted(edge_bc.items(), key=lambda x: x[1], reverse=True)[:5]:
#     print(edge, ":", score)