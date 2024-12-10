import hashlib
from kv_server.crypto.hasher import Hasher


class MD5Hasher(Hasher):

    SUPPORTED_ACTIONS = [
        'encrypt',
    ]

    def encrypt(self, data, *args, **kwargs):
        return hashlib.md5(data.encode('UTF-8')).digest()
