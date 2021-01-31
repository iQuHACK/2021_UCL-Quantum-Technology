# Basic Problems 

## Problems 1 to 4

Please see Solutions_01_to_04.pdf for the algebraic and numerical computation of the algorithms on Slides 19 and 21.

## Problem 5

The algebraic verification of Slide 29 is attached as Solutions_05.pdf.

## Problem 6

Solutions_06.pdf shows the verification of the answers shown on slide 30.  There are only two solutions because two solutions share the same energy.  This is because setting one Qubit to 0 or 1 forces the others to a unique configuration.

## Problem 7

We were able to run the program two_same.py in the Leap IDE without issues and attach a screen shot of the same as Solutions_07.pdf.

## Problem 8 

The algebra in slide 40 is worked out in Solutions_08.pdf.

## Problem 9

We implemented the QUBO in slide 40 as a Python program exactly_one.py.  
The results were as shown in Slide 41.  Alternatively alt_solution9.py uses Qiskit to evaluate the solution.

##  Problem 10

We implemented the QUBO in slide 48 as a Python program boxes.py.  As expected boxes 1 and 3 when combined together had the lowest energy.  Alternatively alt_solution10.py uses Qiskit to evaluate the solution.

## Problem 11

Solutions_11.jpeg shows the algebra and is checked back to slide 57.  Alternatively alt_solution11.py uses Qiskit to evaluate the solution.

## Problem 12

clique.py is implemented for the graph partitioning problem. 
The results correctly identify six solutions, which agrees since this represents the 4!/(2!*2!) symmetries in choosing two objects from four.

## Problem 13

The constant term on slide evaluates as 1.5 * (4)^2/4 = 6.  When we add this we get 4, which is the expected number of vertices for each clique.

##  Problem 14

New programs exactly_one_hybrid.py, boxes_hybrid.py and clique_hybrid.py submit the code from earlier on a hybrid solver.  
In each case only one solution is returned.  This solution has the same energy as the lowest solution found from the exact solver.

##  Problem 15

Program knapsack.py is written.  We agree with the results on slides 74.  For slide 74 we get slightly different answers.  Maybe the datafile has changed.

## Problem 16

The program in slide 89 is coded as graph_partitioning.py.  We get the results shown in Slide 90.  
