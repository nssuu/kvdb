

class Ring(object):

    def __init__(self, *args, **kwargs):
        self.coordinator = kwargs.get('coordinator')

    def upsert_node_by_key(self, key, *args, **kwargs):
        return self.coordinator.upsert_node_by_key(key, *args, **kwargs)

    def upsert_node(self, node, *args, **kwargs):
        return self.coordinator.upsert_node(node, *args, **kwargs)

    def get_nearest(self, key, *args, **kwargs):
        return self.coordinator.get_nearest(key, *args, **kwargs)
