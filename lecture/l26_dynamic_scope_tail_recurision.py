"""
lecture 26
Dynamic scope
functional programming
"""

## lexical scope
# the parent of a frame is the environment in which a procedure was ``defined``
## dynamic scope 
# the parent of a frame is the environment in which a procedure was ``called``

## functional programming
# all functions are pure functions
# no re-assignment and no mutable data types
# name-value bindings are permanent
# advantages: (1)the value of an expression is independent of the order in which sub-expressions are evaluated (2) sub-expressions can safely be evaluated in parallel or on demand (3) referential transparency: the value of an expression does not change when we substitute one of its sub-expression with the value of the sub-expression

# no for/while statements
# need tail recursion
# tail call: call expression in a tail context -> the last body sub-expression in a lambda expression
# tail call optimization: the return value of the tail call is the return value of the current procedure call -> tail calls should not increase the environment size





