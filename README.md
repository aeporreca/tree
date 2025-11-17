# The `tree` Python library

A simple (arbitrary arity) tree library in Python for an introductory computer science course with Python code, with a minimum of useful error messages.

The following examples show the usage of the library:

```python
from tree import Leaf, Node, is_leaf, key, arity, child


T = Node(1, [
        Node(2, [
            Leaf(5),
            Leaf(6)
        ]),
        Node(3, [
            Node(7, [
                Leaf(8)
            ])
        ]),
        Leaf(4)
    ])


def tree_size(T):
    if is_leaf(T):
        return 0
    n = arity(T)
    s = 0
    for i in range(n):
        s = s + tree_size(child(T, i))
    return s


def tree_flip(T):
    k = key(T)
    if is_leaf(T):
        return Leaf(k)
    n = arity(T)
    C = []
    for i in range(n):
        S = tree_flip(child(T, i))
        C.append(S)
    return Node(k, C)
```
