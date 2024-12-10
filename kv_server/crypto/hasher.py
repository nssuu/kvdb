
class Hasher(object):

    SUPPORTED_ACTIONS = []

    def __init__(self, *args, **kwargs):
        pass

    def encrypt(self, data, *args, **kwargs):
        raise NotImplementedError

    def decrypt(self, data, *args, **kwargs):
        raise NotImplementedError
