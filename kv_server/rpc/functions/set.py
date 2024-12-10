from kv_client import KVClient


def set(ctx, *args, **kwargs):
    key = args[0]
    successor_addr = ctx.server.ring.get_nearest(key).key
    if ctx.server.addr != successor_addr:
        client = KVClient(
            endpoint=successor_addr,
        )
        return client.set(*args)
    value = args[1]
    return ctx.server.store.set(key, value)
