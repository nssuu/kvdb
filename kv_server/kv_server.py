import threading
from kv_server.rpc import FunctionRegistry
from kv_server.rpc import functions
from kv_server.inet.http.server import HTTPServer
from kv_server.crypto import MD5Hasher
from kv_server.ring import BisectCoordinator
from kv_server.ring import Ring
from kv_server.storage import KVStore


class KVServer(object):

    def __init__(self, *args, **kwargs):
        self.host = kwargs.get('host')
        self.port = kwargs.get('port')
        self.is_serving = False
        self.hasher = MD5Hasher()
        self.ring = Ring(
            coordinator=BisectCoordinator(
                hasher=self.hasher,
                replication_factor=100,
            ),
        )
        self.cluster = kwargs.get('cluster', [])
        replication_factor = kwargs.get('replication_factor', 1)
        for node_addr in self.cluster:
            self.ring.upsert_node_by_key(
                node_addr,
                replication_factor=replication_factor,
            )
        self.store = KVStore()
        self.function_registry = FunctionRegistry(
            server=self,
        )
        self.function_registry.functions['ping'] = functions.ping
        self.function_registry.functions['get'] = functions.get
        self.function_registry.functions['set'] = functions.set
        self.function_registry.functions['has'] = functions.has
        self.function_registry.functions['pop'] = functions.pop
        self.function_registry.functions['list_keys'] = functions.list_keys
        self.function_registry.functions['list_members'] = functions.list_members
        self.function_registry.functions['locate'] = functions.locate
        self.threads = {}

    @property
    def addr(self):
        return f'{self.host}:{str(self.port)}'

    def serve(self, *args, **kwargs):
        http_server = HTTPServer(
            server=self,
            host=self.host,
            port=self.port,
        )
        self.threads['http_server'] = threading.Thread(
            target=http_server.serve,
        )
        for thread in self.threads.values():
            thread.start()
        self.is_serving = True
        for thread in self.threads.values():
            thread.join()

    def stop(self, *args, **kwargs):
        pass
