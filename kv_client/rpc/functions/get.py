from kv_client.rpc import RemoteFunction


def get(endpoint, key, default_value=None):
    remote_function = RemoteFunction(endpoint, 'get', key, default_value=default_value)
    result = remote_function.invoke()
    return result
