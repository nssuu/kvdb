from kv_client.rpc import RemoteFunction


def has(endpoint, key):
    remote_function = RemoteFunction(endpoint, 'has', key)
    result = remote_function.invoke()
    return result
