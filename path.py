from http.server import HTTPServer, BaseHTTPRequestHandler#path
from urllib import parse
import io
import cgi
import psycopg2
import json

conn = psycopg2.connect(
    database="postgres",
    host="127.0.0.1",
    port="5432",
    user="postgres",
    password="18312100"
)
conn.autocommit = True


class GetHandler(BaseHTTPRequestHandler):
  qu = """SELECT * FROM public.day ORDER BY id ASC """
  def do_GET(self):
        self.parsed_path = parse.urlparse(self.path)
        cur = conn.cursor()
        self.query = self.parsed_path.qu
        cur.execute()
        data = cur.fetchall(self.query)
        self.send_response(200)
        self.send_header('Content-Type',
                         'application/json')
        self.end_headers()
        data = json.dumps(data)
        self.wfile.write(data.encode('utf-8'))

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()