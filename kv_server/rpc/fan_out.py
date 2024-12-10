from kv_client import KVClient
from kv_server.exec import ParallelExecutor


class FanOut(object):

    @classmethod
    def request(cls, endpoints, lazy_function):
        lazy_functions = []
        for endpoint in endpoints:
            lazy_functions.append(
                cls.wrap_lazy_function(endpoint, lazy_function),
            )
        results = ParallelExecutor.execute(lazy_functions)
        return results

    @classmethod
    def wrap_lazy_function(cls, endpoint, lazy_function):
        def wrapper():
            client = KVClient(
                endpoint=endpoint,
            )
            return lazy_function(client)
        return wrapper
