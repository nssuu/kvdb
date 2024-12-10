from kv_client.rpc import RemoteFunction


def set(endpoint, key, value):
    remote_function = RemoteFunction(endpoint, 'set', key, value)
    result = remote_function.invoke()
    return result
