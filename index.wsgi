def application(environ, start_response):
    body = b'Helloworld!\n'
    status = '200 ok'
    headers = [('content-type', 'text/plain')]
    start_response(status, headers)
    return [body]
