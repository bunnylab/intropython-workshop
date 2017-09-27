#!/usr/bin/env/python

friend_counts = {'john':105, 'joanna':999, 'jesus':2100000000, 'zoe':32}
important_people = []
unimportant_people = []

if( friend_counts['zoe']>=100):
	important_people.append('zoe')
elif( friend_counts['zoe']<=100):
	unimportant_people.append('zoe')
	
print("Important: ",important_people)
print("Unimportant: ", unimportant_people)