#!/usr/bin/env/python

friend_counts = {'john':105, 'joanna':999, 'jesus':2100000000, 'zoe':32}
important_people = []
unimportant_people = []

for name in friend_counts:
	if( friend_counts[name]>=100):
		important_people.append(name)
	elif( friend_counts[name]<=100):
		unimportant_people.append(name)
	
print("Important: ",important_people)
print("Unimportant: ", unimportant_people)