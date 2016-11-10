"""
lecture 35
distributed computing
"""

# consists of multiple programs running on multiple computers that together coordinate to perform some task

# computation is performed in ``parallel`` by many computers
# information can be restricted to certain computers
# redundancy and geographic diversity improve reliability

# map reduce

## mapper
import sys
from mr import emit


def emit_vowels(line):
	for vowel in 'aeiou':
		count = line.count(vowel)
		if count > 0:
		emit(vowel, count) # emit function outputs a key and value as a line of text to standard output 

for line in sys.stdin:
	emit_vowels(line) # mapper inputs are lines of text provided to standard input
