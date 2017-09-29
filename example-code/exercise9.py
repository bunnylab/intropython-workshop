#!/usr/bin/env python
import urllib.request

def word_count(input_string):
	unique_words = {}
	word_list = input_string.split(' ')
	
	for word in word_list:
		word = word.strip()
		if word in unique_words:
			unique_words[word] += 1
		else:
			unique_words[word] = 1
			
	return unique_words
	
response = urllib.request.urlopen('http://python.org')
html = response.read().decode('utf-8')
unique = word_count(html)

with open('frequency_output.txt', 'w') as output:
	for key in unique:
		output.write(key + ": " + str(unique[key]) + "\n" )