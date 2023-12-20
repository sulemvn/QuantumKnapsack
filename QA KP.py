#!/usr/bin/env python3

from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import BinaryQuadraticModel




# Set up scenario
import numpy as np





test = int(input("Press ´1´ for 7 items ´2´for 21 items and ´3´ for 50 items: "))


if test == 1:
	
	max_weight = 70
	weight =[12,27,11,17,20,10,15]
	value=[35,85,30,50,70,80,55]
	i = 7
	objects = np.arange(i)
	
	
if test == 2:
	
	max_weight = 150
	weight =[12,27,11,17,20,10,15,95,70,85,31,100,1,7,53,35,11,64,26,4,34]
	value=[35,85,30,50,70,80,55,77,44,15,67,75,91,2,46,16,68,35,53,84,85]
	i = 21
	objects = np.arange(i)
	
	
	
if test == 3:
	
	max_weight = 650
	weight =[12,27,11,17,20,10,15,95,70,85,31,100,1,7,53,35,11,64,26,4,34,12,27,11,17,20,10,15,95,70,85,31,100,1,7,53,35,11,64,26,4,34,7,53,35,11,64,26,4,34]
	value=[35,85,30,50,70,80,55,77,44,15,67,75,91,2,46,16,68,35,53,84,85,35,85,30,50,70,80,55,77,44,15,67,75,91,2,46,16,68,35,53,84,85,2,46,16,68,35,53,84,85]
	i = 50
	objects = np.arange(i)
	
# Build a variable for each object
x=[]

for o in objects:
    x.append(f'O{o}') 
	
	
# Create bqm
bqm = BinaryQuadraticModel("BINARY")


#Objective
for o in objects:
    bqm.add_variable(x[o], -1*value[o])
	
	
	
# Add Constraint
c1 = [(x[o], weight[o]) for o in objects]
bqm.add_linear_equality_constraint(c1,constant = -max_weight, lagrange_multiplier=100)


sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=1000)

sample = sampleset.first.sample
energy = sampleset.first.energy



total_value = 0
total_weight = 0
printout = ""

# Creat print out
for o in objects:
    printout += str(sample[x[o]])
    total_value += sample[x[o]]*value[o]
    total_weight += sample[x[o]]*weight[o]


print(printout)
print("\nTotal weight:\t", total_weight)
print("\nTotal Value:\t", total_value)
print("\nEnergy:\t", energy)


