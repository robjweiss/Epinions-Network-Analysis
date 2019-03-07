# Author: Rob Weiss
# Description: This program calculates statistics about the network fromed between reviewers on epinions.com
import networkx as nx

# Reads in the graph from the CSV file
G = nx.read_weighted_edgelist('./data/epinions_small.csv', delimiter=',')

numEdges = G.number_of_edges()
print('Edges in network:', numEdges)

selfLoops = len(list(G.nodes_with_selfloops()))
print('Self-loops:', selfLoops)

totEdges = numEdges - selfLoops
print('Edges used - TotEdges:', totEdges)

trustEdges = 0
distrustEdges = 0
# Iterates over all edges in the network and counts the trusted and distrusted edges
for attribute in nx.get_edge_attributes(G, 'weight').values():
    if (attribute == 1):
        trustEdges += 1
    elif (attribute == -1):
        distrustEdges += 1

probTrust = round(trustEdges / totEdges, 2)
print('Trust edges:', trustEdges, '\t', 'Probability:', probTrust)

probDistrust = round(1 - probTrust, 2)
print('Distrust edges', distrustEdges, '\t', 'Probability:', probDistrust)

all_cliques = nx.enumerate_all_cliques(G)
triad_cliques = [clique for clique in all_cliques if len(clique) == 3] # Triads (all cliques of size 3)
numTriads = len(triad_cliques)
print('Triangles:', numTriads)

# This section calculates the Percent and Nummber of expected triads of each type based on the trusted edges and distrusted edges in the network
print('\nExpected Distribution\nType\t %\t Number')

tttPercentExpected = (trustEdges / totEdges) ** 3
tttNumberExpected = tttPercentExpected * numTriads
print('TTT\t', round(tttPercentExpected * 100, 2), '\t', round(tttNumberExpected, 2))

ttdPercentExpected = (trustEdges / totEdges) ** 2 * (distrustEdges / totEdges) * 3
ttdNumberExpected = ttdPercentExpected * numTriads
print('TTD\t', round(ttdPercentExpected * 100, 2), '\t', round(ttdNumberExpected, 2))

tddPercentExpected = (trustEdges / totEdges) * (distrustEdges / totEdges) ** 2 * 3
tddNumberExpected = tddPercentExpected * numTriads
print('TDD\t', round(tddPercentExpected * 100, 2), '\t', round(tddNumberExpected, 2))

dddPercentExpected = (distrustEdges / totEdges) ** 3
dddNumberExpected = dddPercentExpected * numTriads
print('DDD\t', round(dddPercentExpected * 100, 2), '\t', round(dddNumberExpected, 2))

totalNumberExpected = tttNumberExpected + ttdNumberExpected + tddNumberExpected + dddNumberExpected
totalPercentExpected = tttPercentExpected + ttdPercentExpected + tddPercentExpected + dddPercentExpected
print('Total\t', round(totalPercentExpected * 100, 2), '\t', round(totalNumberExpected, 2))

tttNumberActual = 0
ttdNumberActual = 0
tddNumberActual = 0
dddNumberActual = 0
# Iterates over all of the triads found, determines the type, and increments the total of that type
for triad in triad_cliques:
    node1 = triad[0]
    node2 = triad[1]
    node3 = triad[2]
    edge1 = G[node1][node2]['weight']
    edge2 = G[node1][node3]['weight']
    edge3 = G[node2][node3]['weight']
    total = edge1 + edge2 + edge3

    if (total == 3.0):
        tttNumberActual += 1
    elif (total == 1.0):
        ttdNumberActual += 1
    elif (total == -1.0):
        tddNumberActual += 1
    elif (total == -3.0):
        dddNumberActual += 1

# This section calculates the Percent and Nummber of actual triads of each type based on the actual number of each type of triad in the network
print('\nActual Distribution\nType\t %\t Number')

tttPercentActual = tttNumberActual / numTriads
print('TTT\t', round(tttPercentActual * 100, 2), '\t', tttNumberActual)

ttdPercentActual = ttdNumberActual / numTriads
print('TTD\t', round(ttdPercentActual * 100, 2), '\t', ttdNumberActual)

tddPercentActual = tddNumberActual / numTriads
print('TDD\t', round(tddPercentActual * 100, 2), '\t', tddNumberActual)

dddPercentActual = dddNumberActual / numTriads
print('DDD\t', round(dddPercentActual * 100, 2), '\t', dddNumberActual)

totalNumberActual = tttNumberActual + ttdNumberActual + tddNumberActual + dddNumberActual
totalPercentActual = tttPercentActual + ttdPercentActual + tddPercentActual + dddPercentActual
print('Total\t', round(totalPercentActual * 100, 2), '\t', totalNumberActual)