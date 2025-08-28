import http.server
import socketserver
import json

from validator import validate_post_code
from urllib.parse import parse_qs, urlparse

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        status_code = 200
        o = urlparse(self.path)

        response_data = {"status": "error", "message": "Bad Request."}

        if o.path == "/api/":
            status_code = 400
            query_string = o.query
            query_params = parse_qs(query_string)
            post_code = query_params.get("post_code", None)

            if post_code:
                status_code = 200
                validation_result, validation_message = validate_post_code(post_code[0])    
                response_data = {
                    "status": "error" if not validation_result else "success",
                    "message": validation_message
                }

        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(response_data).encode('utf-8'))


if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    with socketserver.TCPServer((HOST, PORT), MyHandler) as httpd:
        print(f"Server is running on port {PORT}...")
        httpd.serve_forever()