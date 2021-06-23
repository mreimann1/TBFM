#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys
from json import dumps

from melody_t import *

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)
    
    def _send_cors_headers(self):
        """ Sets headers required for CORS """
        # self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")

    def send_dict_response(self, d):
        """ Sends a dictionary (JSON) back to the client """
        self.wfile.write(bytes(dumps(d), "utf8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_POST(self):
        self.send_response(200)
        self._send_cors_headers()
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        dataLength = int(self.headers["Content-Length"])
        data = self.rfile.read(dataLength)

        # Parse request
        path = self.path
        toFind = ".mid"
        index = path.find(toFind)
        melodyname = path[1:index]
        toFind = "swiped="
        index = path.find(toFind)
        swiperesult = path[index+len(toFind):] == "true"
        print(melodyname, "was swiped", ("right" if swiperesult else "left"))

        # Append result of request to file
        f = open("swipedata.txt", "a")
        f.write(""+melodyname+":"+str(swiperesult)+"\n")
        f.close()

        response = {}
        response["status"] = "OK" # TODO: send "melody{index} was {sucessfully|unsuccessfully} swiped {left|right}"
        self.send_dict_response(response)
        

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)