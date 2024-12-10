
class FunctionRegistry(object):

    def __init__(self, *args, **kwargs):
        self.functions = {}
        self.server = kwargs.get('server')

    def invoke(self, f_name, ctx, *args, **kwargs):
        f = self.functions.get(f_name)
        if not callable(f):
            raise RuntimeError(f'function must be callable: {f_name}')
        setattr(ctx, 'server', self.server)
        return f(ctx, *args, **kwargs)
