import flask
from kv_server.rpc import Context


class FlaskHTTPServerDriver(object):

    BAD_REQUEST = {
        'status': 'Error',
        'description': 'Bad request.',
    }

    def __init__(self, *args, **kwargs):
        self.host = kwargs.get('host', '0.0.0.0')
        self.port = kwargs.get('port', 4887)
        self.instance = flask.Flask(__name__)
        self.instance.add_url_rule(
            '/',
            view_func=self._handle_request,
            methods=[
                'POST',
            ],
        )
        self.server = kwargs.get('server')

    def serve(self):
        return self.instance.run(self.host, self.port)

    def _handle_request(self):
        body = flask.request.get_json()
        if not isinstance(body, dict):
            return self.BAD_REQUEST
        f_name = body.get('function')
        if not f_name:
            return self.BAD_REQUEST
        args = body.get('args', [])
        if not isinstance(args, list):
            return self.BAD_REQUEST
        kwargs = body.get('kwargs', {})
        if not isinstance(kwargs, dict):
            return self.BAD_REQUEST
        result = None
        try:
            ctx = Context()
            result = self.server.function_registry.invoke(
                f_name,
                ctx,
                *args,
                **kwargs,
            )
        except Exception as error:
            return {
                'status': 'Error',
                'description': str(error),
            }
        return {
            'status': 'OK.',
            'result': result,
        }
