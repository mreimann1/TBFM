#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys
from json import dumps
import os
from shutil import copyfile

from melody_t import *
from var_defs import *

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
        print(f"index: {index}")
        if (index > 0) :
            melodyname = path[1:index]
            toFind0 = "swiped="
            index0 = path.find(toFind0)
            toFind1 = "&name"
            index1 = path.find(toFind1)
            swiperesult = (path[index0+len(toFind0):] == "true") if (index1 < 0) else (path[index0+len(toFind0):index1] == "true")
            print(melodyname, " was swiped", ("right" if swiperesult else "left"))
            
            # determine username
            toFind2 = "name="
            index2 = path.find(toFind2)
            if (index2 < 0) :
                swipe_filename = DATA_SWIPEDATA
            else:
                username = path[index2+len(toFind2):]
                swipe_filename = f"./tbfm/{username}/{DATA_SWIPEDATA}" 
                print(f"swipe_filename: {swipe_filename}")
            # Append result of request to file
            f = open(swipe_filename, "a+")
            f.write(""+melodyname+":"+str(swiperesult)+"\n")
            f.close()

        # setname request
        path = self.path
        toFind = "setname"
        index = path.find(toFind)
        if (index > 0):
            melodyname = path[1:index]
            toFind = "?name="
            index = path.find(toFind)
            username = 'tbfm/' + path[index+len(toFind):] + '/'
            print(f"setname request received. TODO: make dir: {username}")
            if not os.path.exists(username):
                os.makedirs(username)
                # Copy files over
                copyfile("rules_l.py", username+"rules_l.py")
                copyfile("melody_t.py", username+"melody_t.py")
                copyfile("music_maker.py", username+"music_maker.py")
                copyfile("melody_init.py", username+"melody_init.py")
                copyfile("melody_update.py", username+"melody_update.py")
                copyfile("var_defs.py", username+"var_defs.py")
                os.makedirs(username+"/data")
                os.makedirs(username+"/dumps")
                # TODO: implement run_init
                

        # TODO: implement run_update
        # path = self.path
        # toFind = "setname"
        # index = path.find(toFind)
        # if (index > 0):
        #     melodyname = path[1:index]
        #     toFind = "?name="
        #     index = path.find(toFind)
        #     username = 'tbfm' + path[index+len(toFind):]
        #     print(f"setname request received. TODO: make dir: {username}")
        #     if not os.path.exists(username):
        #         os.makedirs(username)

        response = {}
        response["status"] = "OK" # TODO: send "melody{index} was {sucessfully|unsuccessfully} swiped {left|right}"
        self.send_dict_response(response)
        

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)