from kv_client.rpc import functions


class KVClient(object):

    def __init__(self, *args, **kwargs):
        self.endpoint = kwargs.get('endpoint')
        if not self.endpoint.startswith('http'):
            self.endpoint = f'http://{self.endpoint}'

    def ping(self):
        return functions.ping(self.endpoint)

    def get(self, key, default_value=None):
        return functions.get(self.endpoint, key, default_value=default_value)

    def set(self, key, value):
        return functions.set(self.endpoint, key, value)

    def has(self, key):
        return functions.has(self.endpoint, key)

    def pop(self, key, default_value=None):
        return functions.pop(self.endpoint, key, default_value=default_value)

    def list_keys(self, fan_out_mode=True):
        return functions.list_keys(
            self.endpoint,
            fan_out_mode=fan_out_mode,
        )

    def list_members(self):
        return functions.list_members(self.endpoint)

    def locate(self, key):
        return functions.locate(self.endpoint, key)
