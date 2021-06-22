from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys
import cgi
import string

from rules_l import *
from melody_t import *
import mai # for writing lists to midi files. In the future I can use pretty_midi for this 

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')

    def do_POST (self):
        print ("self.path: " , self.path)
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        print ("ctype: ", ("none" if ctype is None else ctype), " pdict: ", pdict)

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

        

        # self.send_response(200)
        # self.send_header('content-type', 'text/html')
        self.end_headers()

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8080)