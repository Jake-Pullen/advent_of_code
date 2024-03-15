import networkx as nx
from collections import defaultdict

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def create_graph(edge_list):
    graph = nx.DiGraph()
    for node, edges in edge_list.items():
        for edge in edges:
            graph.add_edge(node, edge, capacity=1.0)
            graph.add_edge(edge, node, capacity=1.0)
    return graph

def find_minimum_cut(graph, nodes):
    for source_node in [list(nodes.keys())[0]]:
        for target_node in nodes.keys():
            if source_node != target_node:
                cut_value, (left, right) = nx.minimum_cut(graph, source_node, target_node)
                if cut_value == 3:
                    print(len(left) * len(right))
                    break

data = read_file(r'advent_of_code\2023\25\input.txt')

lines = data.split('\n')
grid = [[char for char in row] for row in lines]

edges = defaultdict(set)
for line in lines:
    start_node, end_nodes = line.split(':')
    for end_node in end_nodes.split():
        edges[start_node].add(end_node)
        edges[end_node].add(start_node)

graph = create_graph(edges)

find_minimum_cut(graph, edges)