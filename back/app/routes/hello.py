from . import api_v1

@api_v1.route('/', methods=['GET'])
def hello():
    return 'Hello, world!'
