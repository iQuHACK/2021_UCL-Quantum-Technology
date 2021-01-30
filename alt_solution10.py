from qiskit.optimization import QuadraticProgram
from qiskit.optimization.algorithms import MinimumEigenOptimizer
from dwave.plugins.qiskit import DWaveMinimumEigensolver

# Specify the problem - in IBM language
qp = QuadraticProgram()
qp.binary_var('x')
qp.binary_var('y')
qp.binary_var('z')

g = 25
qp.minimize(linear={'x': 17 - 3*g, 'y': 21 - 3*g, 'z': 19 - 3*g}, quadratic={'zx': g*2, 'yx': g*2, 'zy': g*2})


dwave_mes = DWaveMinimumEigensolver()

optimizer = MinimumEigenOptimizer(dwave_mes)

result = optimizer.solve(qp)

print(result.samples)