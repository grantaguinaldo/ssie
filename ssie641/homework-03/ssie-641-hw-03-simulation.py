import pycxsimulator
from pylab import *
import networkx as nx
import numpy as np

populationSize = 500
linkProbability = 0.01
initialInfectedRatio = 0.01
#infectionProb = 0.2 #made this dynamic, via a differential equation. 
recoveryProb = 0.8 
linkCuttingProb = 0.1
vax_const = 0.95

susceptible = 0
infected = 1

infected_count_list = []

def initialize():
    global time, network, positions, nextNetwork, x_i, results, infected_count_list
    x_i = 1
    results = [x_i]

    time = 0
    
    network = nx.erdos_renyi_graph(populationSize, linkProbability) #can make a BA network.
    #network = nx.barabasi_albert_graph(n=500, m=200, seed=42)

    positions = nx.random_layout(network)

    for i in network.nodes:
        if random() < initialInfectedRatio:
            network.nodes[i]['state'] = infected
        else:
            network.nodes[i]['state'] = susceptible

    nextNetwork = network.copy()

def observe():
    global x_i, results, infected_count_list
    results.append(x_i)

    cla()
    nx.draw(network,
            pos = positions,
            node_color = [network.nodes[i]['state'] for i in network.nodes],
            cmap = cm.Wistia,
            vmin = 0,
            vmax = 1)
    axis('image')
    title('t = ' + str(time))


def update():
    global time, network, nextNetwork, x_i, results, infected_count_list
    x_i = vax_const * results[-1]

    

    vax_rate = 1-x_i #growing vax rate.

    #print(x_i)

    time += 1
    infected_count = 0

    for i in network.nodes:
        if network.nodes[i]['state'] == susceptible:
            nextNetwork.nodes[i]['state'] = susceptible
            for j in network.neighbors(i):
                if network.nodes[j]['state'] == infected:
                    if random() < x_i: #infectionProb
                        nextNetwork.nodes[i]['state'] = infected
                        infected_count += 1
                        break
                    else: # adaptive link cutting behavior
                        if random() < linkCuttingProb:
                            if nextNetwork.has_edge(i, j):
                                nextNetwork.remove_edge(i, j)
        else:
            if random() < recoveryProb:
                nextNetwork.nodes[i]['state'] = susceptible
            else:
                nextNetwork.nodes[i]['state'] = infected
                infected_count += 1

    del network
    network = nextNetwork.copy()
    infected_count_list.append(infected_count)

    print(infected_count_list)

pycxsimulator.GUI().start(func=[initialize, observe, update])
