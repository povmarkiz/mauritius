import http.server, socketserver, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 3000), Handler) as httpd:
    httpd.serve_forever()
