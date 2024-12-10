import requests


class RemoteFunction(object):

    STATUS_OK = 'OK.'

    def __init__(self, endpoint, f_name, *args, **kwargs):
        self.endpoint = endpoint
        self.f_name = f_name
        self.args = args
        self.kwargs = kwargs

    def invoke(self):
        response = requests.post(
            self.endpoint,
            json={
                'function': self.f_name,
                'args': self.args,
                'kwargs': self.kwargs,
            },
        )
        body = response.json()
        status = body.get('status')
        if status != self.STATUS_OK:
            description = body.get('description')
            raise RuntimeError(description)
        result = body.get('result')
        return result


