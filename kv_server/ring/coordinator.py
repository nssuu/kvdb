

class Coordinator(object):

    def upsert_node_by_key(self, key, *args, **kwargs):
        raise NotImplementedError

    def upsert_node(self, node, *args, **kwargs):
        raise NotImplementedError

    def get_nearest(self, key, *args, **kwargs):
        raise NotImplementedError
