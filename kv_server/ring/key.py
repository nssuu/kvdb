

class Key(object):

    @classmethod
    def to_digest(cls, key, hasher):
        return hasher.encrypt(key)
