

class KVStore(object):

    def __init__(self, *args, **kwargs):
        self.data = {}

    def get(self, key, default_value=None):
        return self.data.get(key, default_value)

    def set(self, key, value):
        self.data[key] = value

    def has(self, key):
        return key in self.data

    def pop(self, key, default_value=None):
        return self.data.pop(key, default_value)

    def list_keys(self):
        return list(self.data.keys())
