from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field

from .node import Node


class NodeShapeType(metaclass=ABCMeta):
    pass


@dataclass
class MutableNodeShapeType(metaclass=ABCMeta):
    _nodefactory: callable

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        self.clear_nodes()
        for n in nodes:
            self.add_node(n)
        return self

    def create_node(self, *args, **kwargs):
        return self._nodefactory(self, *args, **kwargs)

    def insert_node(self, index, node):
        if node not in self.nodes:
            if node.master is not None:
                node.master.remove_node(node)
            node.master = self
            self.nodes.insert(index, node)
        return self

    def add_node(self, node):
        return self.insert_node(-1, node)

    def new_node(self, *args, **kwargs):
        node = create_node(*args, **kwargs)
        self.add_node(node)
        return node

    def remove_node(self, node):
        if node.master is self:
            node.master = None
        if node in self._nodes:
            self._nodes.remove(node)
        return self

    def pop_node(self, index=-1):
        node = self._nodes[index]
        self.remove_node
        return node

    def clear_nodes(self):
        for n in self._nodes:
            self.remove_node(n)
        return self


@dataclass
class NodeLineShapeType(metaclass=ABCMeta):
    _nodelinefactory: callable

    def nodeline(self, index):
        return _nodelinefactory(
            self[index], self[index+1]
            )

    def iter_nodelines(self):
        length = len(self)
        return (
            self.nodeline(i) for i in range(length-1)
            )


@dataclass
class NodeShape(NodeShapeType):
    _nodes = list[Node] = field(default_factory=list)

    @property
    def nodes(self):
        return self._nodes

    def __getitem__(self, index):
        return self._nodes[index]

    def __contains__(self, node):
        return node in self._nodes

    def __iter__(self):
        return iter(self._nodes)

    def __len__(self):
        return len(self._nodes)
