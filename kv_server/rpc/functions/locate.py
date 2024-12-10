
def locate(ctx, *args, **kwargs):
    key = args[0]
    return ctx.server.ring.get_nearest(key).key
