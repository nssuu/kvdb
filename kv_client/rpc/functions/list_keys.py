from kv_client.rpc import RemoteFunction


def list_keys(endpoint, fan_out_mode=True):
    remote_function = RemoteFunction(
        endpoint,
        'list_keys',
        fan_out_mode=fan_out_mode,
    )
    result = remote_function.invoke()
    return result
