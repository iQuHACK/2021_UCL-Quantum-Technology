
from networkx import nx
import dwave_networkx as dnx
import dimod
from dimod import DiscreteQuadraticModel
from dwave.system import LeapHybridDQMSampler
from dwave.system import LeapHybridSampler

from dimod import DiscreteQuadraticModel
from dwave.system import LeapHybridDQMSampler
from networkx import nx

lagrange = 10

num_colors = 1  #only one colour for travelling salesman
colors = range(num_colors)
dqm = DiscreteQuadraticModel()
G = nx.Graph()
G.add_weighted_edges_from({ (0, 1, 1), 
                            (0, 2, 50),
                            (0, 3, 51), 
                            (1, 2, 1),
                            (1, 3, 2),
                            (2, 3, 1)})
#G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 6)])
n_edges = len(G.edges)
for p in G.nodes:
    dqm.add_variable(num_colors, label=p)
for p in G.nodes:
    dqm.set_linear(p, colors)
#for p0, p1 in G.edges:
#    dqm.set_quadratic(p0, p1, {(c, c): G.weights})
dqm.set_quadratic(0, 1, {(1, 1): 1})
dqm.set_quadratic(0, 2, {(1, 1): 50})
dqm.set_quadratic(0, 3, {(1, 1): 51})
dqm.set_quadratic(1, 2, {(1, 1): 1})
dqm.set_quadratic(1, 3, {(1, 1): 2})
dqm.set_quadratic(1, 3, {(1, 1): 1})

sampler = LeapHybridDQMSampler()
sampleset = sampler.sample_dqm(dqm)
sample = sampleset.first.sample
energy = sampleset.first.energy
valid = True
for edge in G.edges:
    i, j = edge
    if sample[i] == sample[j]:
        valid = False
        break
print("Solution: ", sample)
print("Solution energy: ", energy)
print("Solution validity: ", valid)

#CASE = "EXACT"

#dqm = DiscreteQuadraticModel()

print(dnx.traveling_salesperson(G, LeapHybridDQMSampler(), start=0))

#print(dnx.traveling_salesperson(G, dimod.ExactSolver(), start=0))