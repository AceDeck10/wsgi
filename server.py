#******************************************************************************
# wsgi
# 
# Python source code for a simple Web Server Gateway Interface 
#
# @author Austine D. Odhiambo
#
#******************************************************************************

def app(environ, start_response):
    response_body = 'Request method: %s' % environ['REQUEST_METHOD']

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)

    return[response_body]