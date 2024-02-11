from http.server import HTTPServer, SimpleHTTPRequestHandler
from multiprocessing import Process

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(CORSRequestHandler, self).end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()


class HLS_SERVER:
    def __init__(self,port) -> None:
        self.port = port
        self.host = '0.0.0.0'
        self.__process = Process(target= HTTPServer,args=((self.host,self.port),CORSRequestHandler))
    def start(self):
        self.__process.start()
    def stop(self):
        self.__process.kill()

