from qiskit.optimization import QuadraticProgram
from qiskit.optimization.algorithms import MinimumEigenOptimizer
from dwave.plugins.qiskit import DWaveMinimumEigensolver

# Specify the problem - in IBM language
qp = QuadraticProgram()
qp.binary_var('x')
qp.binary_var('y')
qp.binary_var('z')
qp.binary_var('w')

g = 1.5
v = 4

qp.minimize(linear={'x': 3-3*g, 'y': 3-3*g, 'z': 3-3*g, 'w' : 3-3*g}, quadratic={'wx': (2*g - 2)*2, 'zx': (2*g - 2), 'yx': (2*g - 2), 'wy' : (2*g - 2), 'zy': (2*g - 2), 'wz' : (2*g - 2)})


dwave_mes = DWaveMinimumEigensolver()

optimizer = MinimumEigenOptimizer(dwave_mes)

result = optimizer.solve(qp)

print(result.samples)