#!/usr/bin/env python3

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:56:50 2022

@author: sulemanhersi
"""
import itertools
import more_itertools 
import numpy as np
import time



# Set up scenario

z = int(input("Press ´1´ for 7 items ´2´for 21 items and ´3´ for 50 items: "))

if z == 1:
	
	max_weight = 70
	weight =[12,27,11,17,20,10,15]
	value=[35,85,30,50,70,80,55]
	i = 7
	objects = np.arange(i)
	
	
if z == 2:
	
	max_weight = 150
	weight =[12,27,11,17,20,10,15,95,70,85,31,100,1,7,53,35,11,64,26,4,34]
	value=[35,85,30,50,70,80,55,77,44,15,67,75,91,2,46,16,68,35,53,84,85]
	i = 21
	objects = np.arange(i)
	
	
	
if z == 3:
	
	max_weight = 650
	weight =[12,27,11,17,20,10,15,95,70,85,31,100,1,7,53,35,11,64,26,4,34,12,27,11,17,20,10,15,95,70,85,31,100,1,7,53,35,11,64,26,4,34,7,53,35,11,64,26,4,34]
	value=[35,85,30,50,70,80,55,77,44,15,67,75,91,2,46,16,68,35,53,84,85,35,85,30,50,70,80,55,77,44,15,67,75,91,2,46,16,68,35,53,84,85,2,46,16,68,35,53,84,85]
	i = 68
	objects = np.arange(i)
	
	
	
	
	
	
	
g = 0

solution_weight = []
solution_value = []

print("START")
start_time = time.time()
# Run through all possible combinations
n = i

knapsack = itertools.product([0,1], repeat=n)
knapsack_combo = list(knapsack)
valid_combo = []


# Check if the combination is valid

while g < len(knapsack_combo):
	
	index = more_itertools.locate(knapsack_combo[g], lambda x: x == 1)
	
	items_picked = list(index)
	
	i = 0
	
	check_weight = 0
	check_value = 0
	
	if not items_picked:
		print()
		
	else:
		
		while i < len(items_picked):
			
			check_weight = check_weight + weight[items_picked[i]]
			check_value = check_value + value[items_picked[i]]
			
			
			i = i +1
			
		if check_weight == max_weight:
			
				solution_weight.append(check_weight)
				solution_value.append(check_value)
				valid_combo.append(knapsack_combo[g])
			
			
			
			
			
	g = g + 1
	
	
# Find the best combination
g = 0
best_combo = 0
all_best_combo = []
check_value = 0
check_weight = 0

while g < len(solution_value):
	
	
	if check_weight <= solution_weight[g] and check_value <= solution_value[g]:
		
		check_value = solution_value[g]
		check_weight = solution_weight[g]
		
		best_combo = g
		
		
		
		
		
	g = g +1
	
g = 0    
while  g < len(valid_combo):
	
	if check_weight == solution_weight[g] and check_value == solution_value[g]:
		
		all_best_combo.append(valid_combo[g])
		
	g = g + 1
	
print(time.time() - start_time,"seconds")
print(weight)
print()
print(value)
print()
print(all_best_combo)
print()    
print(valid_combo[best_combo])
print()
print(solution_weight[best_combo])
print()
print(solution_value[best_combo])

	

