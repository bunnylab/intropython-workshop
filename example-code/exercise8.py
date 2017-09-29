#!/usr/bin/env python

def remover(input_string):
	output_string = ""
	for i in range(len(input_string)):
		if( (i%2)==0 ):
			output_string = output_string + input_string[i]
	
	return output_string
	

test_string = "abcdefghijklmnop"
print( remover(test_string) )