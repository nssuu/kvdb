import bisect
from kv_server.ring.coordinator import Coordinator
from kv_server.ring.key import Key
from kv_server.ring.node import Node


class BisectCoordinator(Coordinator):

    def __init__(self, *args, **kwargs):
        self.nodes = {}
        self.vnodes = {}
        self.sorted_vdigests = []
        self.hasher = kwargs.get('hasher')
        self.replication_factor = kwargs.get('replication_factor', 0)
        if self.replication_factor < 1:
            self.replication_factor = 1

    def _get_node_by_key(self, key):
        return self.nodes.get(key)

    def _add_vnode(self, vnode):
        vdigest = vnode.get_digest(self.hasher)
        self.vnodes[vdigest] = vnode
        bisect.insort_right(self.sorted_vdigests, vdigest)

    def upsert_node_by_key(self, key, *args, **kwargs):
        node = Node(
            key=key,
        )
        return self.upsert_node(node, *args, **kwargs)

    def upsert_node(self, node, *args, **kwargs):
        existing_node = self._get_node_by_key(node.key)
        if existing_node:
            return
        self.nodes[node.key] = node
        replication_factor = kwargs.get(
            'replication_factor',
            self.replication_factor,
        )
        for vnode_idx in range(replication_factor):
            vkey = f'{node.key}-{vnode_idx}'
            vnode = Node(
                key=vkey,
                proxy_key=node.key,
            )
            self._add_vnode(vnode)

    def get_successor_index(self, key, *args, **kwargs):
        digest = Key.to_digest(key, self.hasher)
        index = bisect.bisect_right(self.sorted_vdigests, digest)
        if index >= len(self.sorted_vdigests):
            index = 0
        return index

    def get_nearest(self, key, *args, **kwargs):
        successor_index = self.get_successor_index(key)
        successor_vdigest = self.sorted_vdigests[successor_index]
        vnode = self.vnodes.get(successor_vdigest)
        if vnode.proxy_key:
            node = self.nodes.get(vnode.proxy_key)
            return node
        return vnode
