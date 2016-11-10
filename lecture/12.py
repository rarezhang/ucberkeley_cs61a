# Trees

nested_list = [[1, 2], [],
               [[3, False, None],
                [4, lambda: 5]]]

# A tree of integers
tree = [[1, [2], 3, []], [[4], [5, 6]], 7]

def is_leaf(tree):
    return type(tree) != list

def count_leaves(tree):
    """Count the leaves of a tree.

    >>> count_leaves(tree)
    7
    """
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in tree]
        return sum(branch_counts)

def apply_to_leaves(map_fn, tree):
    """Apply map_fn to all leaves of tree, constructing another tree.

    >>> five = [[1, 2], [3, [4, 5]], 6]
    >>> apply_to_leaves(lambda x: x*x, five)
    [[1, 4], [9, [16, 25]], 36]
    """
    if is_leaf(tree):
        return map_fn(tree)
    else:
        return [apply_to_leaves(map_fn, b) for b in tree]

def flatten(tree):
    """Return a list containing the leaves of tree.

    >>> flatten(tree)
    [1, 2, 3, 4, 5, 6, 7]
    """
    if is_leaf(tree):
        return [tree]
    else:
        return sum([flatten(b) for b in tree], [])

pangram = [['the', 'quick', 'brown', 'fox'],
           ['jumps', 'over', 'a', 'lazy', 'dog']]

def right_binarize(tree):
    """Return a right-branching binary tree with the structure of the input.

    >>> right_binarize([1, 2, 3, 4, 5, 6, 7])
    [1, [2, [3, [4, [5, [6, 7]]]]]]
    >>> right_binarize(pangram)
    [['the', ['quick', ['brown', 'fox']]], ['jumped', ['over', ['a', ['lazy', 'dog']]]]]
    """
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]

# Demo of the Berkeley Parser:
# http://tomato.banatao.berkeley.edu:8080/parser/parser.html 

def dict_demos():
    numerals = {'I': 1.0, 'V': 5, 'X': 10}
    numerals['X']
    numerals.values()
    list(numerals.values())
    sum(numerals.values())
    dict([(3, 9), (4, 16), (5, 25)])
    numerals.get('A', 0)
    numerals.get('V', 0)
    {x: x*x for x in range(3,6)}

    {1: 2, 1: 3}
    {[1]: 2}
    {1: [2]}

