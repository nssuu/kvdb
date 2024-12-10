from kv_client.rpc import RemoteFunction


def ping(endpoint):
    remote_function = RemoteFunction(endpoint, 'ping')
    result = remote_function.invoke()
    return result
