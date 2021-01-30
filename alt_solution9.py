
from qiskit.optimization import QuadraticProgram
from qiskit.optimization.algorithms import MinimumEigenOptimizer
from dwave.plugins.qiskit import DWaveMinimumEigensolver

# Specify the problem - in IBM language
qp = QuadraticProgram()
qp.binary_var('r')
qp.binary_var('g')
qp.binary_var('b')

qp.minimize(linear={'r': -1, 'g': -1, 'b': -1}, quadratic={'br': 2, 'gr': 2, 'bg': 2})


dwave_mes = DWaveMinimumEigensolver()

optimizer = MinimumEigenOptimizer(dwave_mes)

result = optimizer.solve(qp)

print(result.samples)

