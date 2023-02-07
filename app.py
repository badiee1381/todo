from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse
import io
import cgi
import psycopg2
import json
import time

conn = psycopg2.connect(
    database="postgres",
    host="127.0.0.1",
    port="5432",
    user="postgres",
    password="18312100"
)
conn.autocommit = True


class Handler(BaseHTTPRequestHandler):
  def do_GET(self):
        
        cur = conn.cursor()
        cur.execute("""SELECT * FROM public.day ORDER BY id ASC """)
        data = cur.fetchall()
        self.send_response(200)
        self.send_header('Content-Type',
                         'application/json')
        self.end_headers()
        data = json.dumps(data)
        self.wfile.write(data.encode('utf-8'))

'''
def do_POST(self):
         out = io.TextIOWrapper(
            self.wfile,
            encoding='utf-8',
            line_buffering=False,
            write_through=True,
        )
         out.write('Path: {}\n'.format(self.path))
         cursor = conn.cursor()
         cursor.execute("""INSERT INTO public.day value(1,'dad',true,true)""")
         conn.commit()
         print("Records inserted........")
         conn.close()
         self.send_response(200)
         self.send_header("Content-type",'application/json')
         self.end_headers()
         data = json.dumps(data)
         self.wfile.write(data.encode('utf-8'))
         
'''
if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), Handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()