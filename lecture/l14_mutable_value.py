"""
lecture 14
Mutable Values
Immutable Values 
"""
# mutation
suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()  # remove the last item
suits.remove('string')
print(suits)
suits.append('cup')
suits.extend(['sword', 'club'])
print(suits)
suits[2] = 'spade'
suits[:2] = ['heart','dimond']
print(suits)


numerals = {'i':1, 'v':5, 'x':10}
print(numerals)
numerals['x'] = 11 # change 
numerals['l'] = 9  # add
print(numerals)
numerals.pop('x') # remove, return 11
print(numerals)


# Immutable
# protected with mutation

# tuple with one element 
(2,)  # must have ,
(2)  # this is just 2

# add two tuples
(1,2) + (3,4)  # (1, 2, 3, 4)

# can be used as the key of dictionary 
{(1,2):2}

# immutable sequence may still change if it contains a mutable value as an element 
s = ([1,2],3)
s[0][0] = 4  # s = ([4, 2], 3)


# identity operators 
## is -> same object
## == -> equal values
# identical object are always equal values
a = [10]
b = [10]
a == b  # true
a is b  # false
c = b
c.pop() # c = []  and  b = []
c is b  # true 

# encoding string
## ascii
ord('a')
hex(ord('a'))

## unicode standard
# 109,000
# 93 scripts

from unicodedata import name, lookup
name('a')	# 'LATIN SMALL LETTER A'
lookup('WHITE SMILING FACE')
lookup('WHITE FROWNING FACE')
lookup('SKULL AND CROSSBONES')
lookup('SNOWMAN')

## utf-8
# universal character set transformation format
# unicode: correspondence between characters and integers
# utf-8: correspondence between integers and bytes
# byte: 8 bits and can encode any integer 0-255


