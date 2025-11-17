# tree - A simple Python library for (arbitrary arity) trees
# Copyright (C) 2025 Antonio E. Porreca

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from abc import ABC, abstractmethod


class Tree(ABC):

    def __init__(self, key):
        self._key = key

    @property
    def key(self):
        return self._key

    @abstractmethod
    def is_leaf(self):
        ...

    @abstractmethod
    def arity(self):
        ...

    @abstractmethod
    def child(self, i):
        ...

    def __eq__(self, other):
        return (self.key == other.key and
                arity(self) == arity(other) and
                all(self.child(i) == other.child(i)
                    for i in range(arity(self))))


class Leaf(Tree):

    def __repr__(self):
        return f'Leaf({self.key!r})'

    def is_leaf(self):
        return True

    def arity(self):
        return 0

    def child(self, i):
        raise IndexError('a leaf has no children')


class Node(Tree):

    def __init__(self, key, children):
        if (not isinstance(children, list) or
            not all(isinstance(T, Tree) for T in children)):
            raise TypeError(f'{children!r} is not a list of trees')
        if not children:
            raise ValueError('a Node must have at least one child')
        super().__init__(key)
        self.children = children

    def __repr__(self):
        return f'Node({self.key!r}, {self.children!r})'

    def is_leaf(self):
        return False

    def arity(self):
        return len(self.children)

    def child(self, i):
        try:
            return self.children[i]
        except IndexError:
            raise IndexError(f'{self!r} has no child number {i!r}')


def key(T):
    if not isinstance(T, Tree):
        raise TypeError(f'{T!r} is not a tree')
    return T.key


def arity(T):
    if not isinstance(T, Tree):
        raise TypeError(f'{T!r} is not a tree')
    return T.arity()


def is_leaf(T):
    if not isinstance(T, Tree):
        raise TypeError(f'{T!r} is not a tree')
    return T.is_leaf()


def child(T, i):
    if not isinstance(T, Tree):
        raise TypeError(f'{T!r} is not a tree')
    if not isinstance(i, int):
        raise TypeError(f'{i!r} is not an integer')
    return T.child(i)
