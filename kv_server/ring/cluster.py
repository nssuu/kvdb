

class Cluster(object):

    DEFAULT_PORT = 5878

    @classmethod
    def from_string(cls, raw):
        normalized_addrs = []
        addrs = raw.split(',')
        for addr in addrs:
            addr = addr.strip()
            host = None
            port = None
            if ':' in addr:
                addr_split = addr.split(':')
                host = addr_split[0]
                port = addr_split[1]
            else:
                host = addr
            if not host:
                raise RuntimeError(
                    f'invalid member address: {addr}',
                )
            if not port:
                port = cls.DEFAULT_PORT
            node_addr = f'{host}:{str(port)}'
            normalized_addrs.append(node_addr)
        return normalized_addrs
