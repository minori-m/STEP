import urllib2
import json

import sys
sys.path.insert(0,'libs')

import networkx as nx

req = urllib2.urlopen("http://alice.fantasy-transit.appspot.com/net?format=json")
js = json.load(req)

Graph = nx.DiGraph()

for i in range(0,5):
    Graph.add_nodes_from(js[i]["Stations"])
    for j in range(0, len(js[i]["Stations"])-1):
        Graph.add_edge(js[i]["Stations"][j],js[i]["Stations"][j+1])
        Graph.add_edge(js[i]["Stations"][j+1],js[i]["Stations"][j])

#print('all paths')

def showpath(dep,arr):
    paths=[]
    for path in nx.all_simple_paths(Graph, source=dep, target=arr):
        paths.append(path)
    return paths

print showpath('City of Charity','Fungal Forest')