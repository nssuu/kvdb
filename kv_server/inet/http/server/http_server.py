from kv_server.inet.http.server.drivers.flask import FlaskHTTPServerDriver


class HTTPServer(object):

    def __init__(self, *args, **kwargs):
        self.driver_class = kwargs.get('driver_class', FlaskHTTPServerDriver)
        self.driver = self.driver_class(*args, **kwargs)

    def serve(self):
        return self.driver.serve()
