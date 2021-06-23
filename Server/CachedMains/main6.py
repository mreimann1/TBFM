#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys

from melody_t import *

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)
    
    def do_POST (self):
        print ("self.path: " , self.path)
        path = self.path
        print ("parsing path: ", path)  # Prints None or the string value of imsi

        toFind = ".mid"
        index = path.find(toFind)
        melodyname = path[1:index]
        toFind = "swiped="
        index = path.find(toFind)
        swiperesult = path[index+len(toFind):] == "true"
        # When ML is integrated it just needs to use `melodyname` and `swiperesult`
        print(melodyname, "was swiped", ("right" if swiperesult else "left"))

        f = open("swipedata.txt", "a")
        f.write(""+melodyname+":"+str(swiperesult)+"\n")
        f.close()

        self.end_headers()
        

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)