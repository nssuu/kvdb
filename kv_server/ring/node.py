from kv_server.ring.key import Key


class Node(object):

    def __init__(self, *args, **kwargs):
        self.key = kwargs.get('key')
        self.proxy_key = kwargs.get('proxy_key')

    def get_digest(self, hasher):
        return Key.to_digest(self.key, hasher)
