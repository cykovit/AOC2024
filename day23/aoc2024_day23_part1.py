from collections import defaultdict
from typing import List, Dict, Set

class NetworkMap:
    def __init__(self, connections):
        self.connections = connections

def load_network_map(filename: str) -> NetworkMap:
    connections = defaultdict(list)
    
    with open('input_day23.txt', 'r') as f:
        for line in f:
            computer1, computer2 = line.strip().split('-')
            connections[computer1].append(computer2)
            connections[computer2].append(computer1)
            
    return NetworkMap(dict(connections))

def find_triplets(network: NetworkMap) -> List[List[str]]:
    triplets = []
    
    for computer, neighbors in network.connections.items():
        for i in range(len(neighbors) - 1):
            for j in range(i + 1, len(neighbors)):
                neighbor1, neighbor2 = neighbors[i], neighbors[j]
                if neighbor1 in network.connections[neighbor2]:
                    triplet = sorted([computer, neighbor1, neighbor2])
                    if any(comp.startswith('t') for comp in triplet):
                        if triplet not in triplets:
                            triplets.append(triplet)
    
    return triplets

network = load_network_map('input_day23.txt')
triplets = find_triplets(network)
print(len(triplets))
