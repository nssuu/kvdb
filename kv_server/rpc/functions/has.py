from kv_client import KVClient


def has(ctx, *args, **kwargs):
    key = args[0]
    successor_addr = ctx.server.ring.get_nearest(key).key
    if ctx.server.addr != successor_addr:
        client = KVClient(
            endpoint=successor_addr,
        )
        return client.has(key)
    return ctx.server.store.has(key)
