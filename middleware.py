from werkzeug.wrappers import Request, Response, ResponseStream


class Middleware():

    """
    basic wsgi middleware

    """
    
    def __init__(self, app):
        self.app = app
        self.__username__ = "admin"
        self.__password__ = "root"

    def __call__(self, environ, start_response):
        request = Request(environ)
        username = request.authorization['username']
        password = request.authorization['password']

        if username == self.__username__ and password == self.__password__:
            environ['user'] = {'name' : 'admin'}
            return self.app(environ, start_response)
        
        res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        return res(environ, start_response)
