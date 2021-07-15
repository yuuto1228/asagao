import http.server
import socketserver
import os

port = int(os.environ.get("PORT", 5000))
os.chdir(os.path.dirname(__file__))

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(('', port), handler)
httpd.serve_forever()
