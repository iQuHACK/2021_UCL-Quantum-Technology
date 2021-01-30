# Copyright 2020 D-Wave Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import dimod

GAMMA = 25

exactsolver = dimod.ExactSolver()

Q = {('X1','X1'): 15,
     ('X2','X2'): 19, 
     ('X3','X3'): 17, 
     ('X1','X2'): GAMMA,
     ('X1','X3'): GAMMA, 
     ('X2','X3'): GAMMA}

results = exactsolver.sample_qubo(Q)

# print the results
for sample, energy in results.data(['sample', 'energy']):
    print(sample, energy)