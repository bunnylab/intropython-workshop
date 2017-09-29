#!/usr/bin/env python

numbers = []

with open('ex7-nums.txt', 'r') as f:
	for line in f:
		numbers.append(float(line))
		
fsum = sum(numbers)
fmean = sum(numbers)/len(numbers)

with open('ex7-out.txt', 'w') as f:
	f.write("Sum: " + str(fsum) + "\n")
	f.write("Mean: " + str(fmean) + "\n")
		