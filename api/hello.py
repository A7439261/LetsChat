from http.server import BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):

    def do_Get(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

