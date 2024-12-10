from kv_server.rpc.fan_in import FanIn
from kv_server.rpc.fan_out import FanOut


def list_keys(ctx, *args, **kwargs):
    fan_out_mode = kwargs.get('fan_out_mode', True)
    if fan_out_mode:
        kwargs['fan_out_mode'] = False
        lazy_list_keys = lambda client: client.list_keys(
            *args,
            **kwargs,
        )
        results = FanOut.request(ctx.server.cluster, lazy_list_keys)
        merged_result = FanIn.merge_lists_sorted(results)
        return merged_result
    return ctx.server.store.list_keys()
