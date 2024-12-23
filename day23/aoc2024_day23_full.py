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

def find_party(network: NetworkMap) -> str:
    possible_party = {}
    
    for start_computer, initial_neighbors in network.connections.items():
        party_computers = [start_computer]
        candidate_computers = initial_neighbors.copy()
        
        while True:
            computers_to_remove = []

            for i in range(len(candidate_computers) - 1):
                for j in range(i + 1, len(candidate_computers)):
                    if candidate_computers[i] not in network.connections[candidate_computers[j]]:
                        computers_to_remove.append(i)
                        break
                if computers_to_remove:
                    break
            
            if not computers_to_remove:
                party_computers.extend(candidate_computers)
                break
            
            candidate_computers = [comp for i, comp in enumerate(candidate_computers) 
                                if i not in computers_to_remove]
        
        party_password = ','.join(sorted(party_computers))
        possible_party[party_password] = len(party_computers)
    
    return max(possible_party.items(), key=lambda x: x[1])[0]

network = load_network_map('input_day23.txt')
triplets = find_triplets(network)
lan_password = find_party(network)

print(f"Part 1 - Sum of computer names starting with t:", len(triplets))
print(f"Part 2 - LAN party password:", lan_password)
