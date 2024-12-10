
class CommandParser(object):

    def __init__(self, *args, **kwargs):
        self.client = kwargs.get('client')

    def parse_line(self, line):
        segments = line.strip().split()
        len_segments = len(segments)
        if len_segments == 0:
            return None
        if len_segments == 1:
            return self.parse_segments_arity_1(*segments)
        if len_segments == 2:
            return self.parse_segments_arity_2(*segments)
        if len_segments == 3:
            return self.parse_segments_arity_3(*segments)
        return self.parse_segments_arity_dynamic(*segments)

    def parse_segments_arity_1(self, *segments):
        command = segments[0].lower()
        if command == 'ping':
            return self.client.ping()
        if command == 'list_keys':
            return self.client.list_keys()
        if command == 'list_members':
            return self.client.list_members()

    def parse_segments_arity_2(self, *segments):
        command = segments[0].lower()
        if command == 'get':
            key = segments[1]
            return self.client.get(key)
        if command == 'has':
            key = segments[1]
            return self.client.has(key)
        if command == 'pop':
            key = segments[1]
            return self.client.pop(key)
        if command == 'locate':
            key = segments[1]
            return self.client.locate(key)

    def parse_segments_arity_3(self, *segments):
        command = segments[0].lower()
        if command == 'get':
            key = segments[1]
            default_value = segments[2]
            return self.client.get(key, default_value=default_value)
        if command == 'set':
            key = segments[1]
            value = segments[2]
            return self.client.set(key, value)
        if command == 'pop':
            key = segments[1]
            default_value = segments[2]
            return self.client.pop(key, default_value=default_value)

    def parse_segments_arity_dynamic(self, *segments):
        return None
