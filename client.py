import sys
import argparse
import kv_client
import kv_client.shell
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
    args, _ = parser.parse_known_args(argv)
    return args


def main(argv):
    args = parse_args(argv)
    client = kv_client.KVClient(endpoint=f'http://{args.host}:{str(args.port)}/')
    command_parser = kv_client.shell.CommandParser(client=client)
    while True:
        sys.stdout.write('>> ')
        sys.stdout.flush()
        line = sys.stdin.readline().strip()
        if line == 'exit;':
            break
        result = None
        try:
            result = command_parser.parse_line(line)
        except Exception as error:
            result = f'ERROR: {str(error)}'
        sys.stdout.write(str(result))
        sys.stdout.write('\n')
        sys.stdout.flush()
    return 0


if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)
