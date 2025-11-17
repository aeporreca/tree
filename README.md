# The `tree` Python library

A simple (arbitrary arity) tree library in Python for an introductory computer science course with Python code.

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


def tree_height(T):
    if is_leaf(T):
        return 0
    else:
        return 1 + max(
            tree_height(child(T, i))
            for i in range(arity(T))
        )


def tree_flip(T):
    if is_leaf(T):
        return Leaf(key(T))
    else:
        return Node(key(T), [
            tree_flip(child(T, i))
            for i in reversed(range(arity(T)))
        ])
```
