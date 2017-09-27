#!/usr/bin/env python

first_str = "I was a lumberjack who was ok"
second_str = "I worked all night and did progressively stranger things all day"

if(len(first_str) > len(second_str) ):
	print(len(first_str), first_str )
elif(len(first_str) < len(second_str) ):
	print(len(second_str), second_str )
else:
	print("I can't decide!!!")