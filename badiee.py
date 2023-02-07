from http.server import HTTPServer,BaseHTTPRequestHandler
import time


HOST = "127.0.0.1"
PORT = 9999

class TestHttp(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1 style='color:purple;'>Roxo</h1></body></html>","utf-8"))

    def do_POST(self):
         self.send_response(200)
         self.send_header("Content-type","text/html")
         self.end_headers()
         date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
         self.wfile.write(bytes('time: "' + date + '"' , "utf-8"))

server = HTTPServer((HOST,PORT),TestHttp)
print("Server is running ...")

server.serve_forever()
server.server_close()
print("server stop ...")






'''
python -m httpserver   
python -m http.server 9999 -b 127.0.0.1
'''


