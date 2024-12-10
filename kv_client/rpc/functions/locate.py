from kv_client.rpc import RemoteFunction


def locate(endpoint, key):
    remote_function = RemoteFunction(endpoint, 'locate', key)
    result = remote_function.invoke()
    return result
