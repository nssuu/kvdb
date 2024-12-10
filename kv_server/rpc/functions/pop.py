from kv_client import KVClient


def pop(ctx, *args, **kwargs):
    key = args[0]
    successor_addr = ctx.server.ring.get_nearest(key).key
    if ctx.server.addr != successor_addr:
        client = KVClient(
            endpoint=successor_addr,
        )
        return client.pop(key, **kwargs)
    default_value = kwargs.get('default_value')
    return ctx.server.store.pop(key, default_value=default_value)
