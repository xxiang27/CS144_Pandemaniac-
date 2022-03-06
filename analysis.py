# -*- coding: utf-8 -*-
"""analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OAI4DQPIzId9W0RmkGcsXGS4sdDvVqeQ
"""

import sys
import json
import random
import networkx as nx
import numpy as np
import copy 
import pandas as pd

import urllib.request
urllib.request.urlretrieve('https://raw.githubusercontent.com/xxiang27/CS144_Pandemaniac-/main/sim.py', 'sim.py')
urllib.request.urlretrieve('https://raw.githubusercontent.com/xxiang27/CS144_Pandemaniac-/main/graph_utils.py', 'graph_utils.py')
import sim 
from graph_utils import *

def retrieve_graphs(graph_names):
  for graph_name in graph_names:
    retrieve_string = 'https://raw.githubusercontent.com/xxiang27/CS144_Pandemaniac-/main/graphs/' + graph_name + ".json"
    filename = graph_name + ".json"
    urllib.request.urlretrieve(retrieve_string, filename)

def katz_centrality(g, node):
  b = nx.katz_centrality(g)
  return b[node]

def clustering_coeff(g,node):
  b = nx.algorithms.cluster.clustering(g)
  return b[node]

def analyze_graph(G):
  analysis = {}
  analysis["avg_clustering"] = nx.algorithms.cluster.average_clustering(G)
  analysis["triangles"] = nx.algorithms.cluster.triangles(G)
  analysis["max_diameter"] = nx.algorithms.distance_measures.diameter(G)
  analysis["avg_diameter"] = nx.average_shortest_path_length(G)
  return analysis 

def compute_nodes_all(filepath, k=None, factor=2):
  filename = filepath.split("/")[-1]
  G = utils.parse_graph(filepath)
  if k is None:
    num_players, k, id = utils.parse_file(filename)
  node_dict = {}
  node_dict["betweenness"] = utils.random_sample_k(G, k, factor, nx.betweenness_centrality)
  # node_dict["katz"] = utils.random_sample_k(G, k, factor, katz_centrality)
  node_dict["clustering_coeff"] = utils.random_sample_k(G, k, factor, nx.algorithms.cluster.clustering(g))
  node_dict["ours"] = utils.random_sample_k(G, k, factor, utils.deg_ndeg_ratio)
  analysis = analyze_graph(G)

  result_dict = sim.run(nx.convert.to_dict_of_dicts(G), node_dict)
  final = {**result_dict, **analysis}
  return final 

def create_data_table(lst_graphs):
  lst_data = []
  for name in lst_graphs:
    lst_data.append(compute_nodes_all("/content/" + name + ".json"))
  print(lst_data)
  df = pd.DataFrame(lst_data)
  return df

lst_graphs = ["2.10.10","2.10.20","2.10.30","2.5.1","4.10.1","4.5.1", "8.10.1", "8.20.1", "8.20.2"
                ,"8.35.1", "testgraph1", "testgraph2"]

retrieve_graphs(lst_graphs)

utils.compute_nodes("/content/2.10.10.json", utils.deg_ndeg_ratio)

# degree distribution of each graph 
# avg clustering coefficient 
# max clustering coefficent 
# max diameter 
# avg diameter 
# number of connected components
#