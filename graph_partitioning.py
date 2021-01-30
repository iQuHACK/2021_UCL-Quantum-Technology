"""Graph partioning program from slide 89"""

from dimod import DiscreteQuadraticModel
from dwave.system import LeapHybridDQMSampler
from networkx import nx

lagrange = 10

num_colors = 4
colors = range(num_colors)
dqm = DiscreteQuadraticModel()
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 6)])
n_edges = len(G.edges)
for p in G.nodes:
    dqm.add_variable(num_colors, label=p)
for p in G.nodes:
    dqm.set_linear(p, colors)
for p0, p1 in G.edges:
    dqm.set_quadratic(p0, p1, {(c, c): lagrange for c in colors})
for p0, p1 in G.edges:
    dqm.set_quadratic(p0, p1, {(c, c): lagrange for c in colors})
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
