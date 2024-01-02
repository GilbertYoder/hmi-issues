from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT=8000
HOST="0.0.0.0"

if __name__ == "__main__":
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()
