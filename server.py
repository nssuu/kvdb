import sys
import argparse
import kv_server
from kv_server.ring import Cluster


def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog='kvserver',
    )
    parser.add_argument(
        '-H',
        '--host',
        dest='host',
        help='Host name',
        default='127.0.0.1',
        required=False,
    )
    parser.add_argument(
        '-P',
        '--port',
        dest='port',
        help='Port number',
        default=Cluster.DEFAULT_PORT,
        required=False,
    )
    parser.add_argument(
        '-C',
        '--cluster',
        dest='cluster',
        help='Cluster members',
        default='',
        required=False,
    )
    parser.add_argument(
        '-R',
        '--replication-factor',
        dest='replication_factor',
        help='Replication factor',
        type=int,
        default=1,
        required=False,
    )
    args, _ = parser.parse_known_args(argv)
    return args


def main(argv):
    args = parse_args(argv)
    cluster = Cluster.from_string(args.cluster)
    server = kv_server.KVServer(
        host=args.host,
        port=args.port,
        cluster=cluster,
        replication_factor=args.replication_factor,
    )
    server.serve()
    return 0


if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)
