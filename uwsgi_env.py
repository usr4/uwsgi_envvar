import os

assert os.getenv('SECRET_KEY') == 'abcdefghijklmnopqrstuvwxyz0123456789'
assert os.getenv('APP_VALUE1') == 'appvalue1'

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]
