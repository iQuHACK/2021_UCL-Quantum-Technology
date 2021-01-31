
from networkx import nx
import dwave_networkx as dnx
import dimod
#from dimod import DiscreteQuadraticModel
#from dwave.system import LeapHybridDQMSampler

from dwave.system import LeapHybridSampler
sampler = LeapHybridSampler()

#CASE = "EXACT"

#dqm = DiscreteQuadraticModel()

G = nx.Graph()
G.add_weighted_edges_from({ (0, 1, 1), 
                            (0, 2, 50),
                            (0, 3, 51), 
                            (1, 2, 1),
                            (1, 3, 2),
                            (2, 3, 1)})


print(dnx.traveling_salesperson(G, sampler, start=0))

print(dnx.traveling_salesperson(G, dimod.ExactSolver(), start=0))