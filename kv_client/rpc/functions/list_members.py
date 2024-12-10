from kv_client.rpc import RemoteFunction


def list_members(endpoint):
    remote_function = RemoteFunction(endpoint, 'list_members')
    result = remote_function.invoke()
    return result
