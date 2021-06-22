#!python
import glob
import os.path

import cherrypy
from cherrypy.lib.static import serve_file

import mimetypes

class Root:
    def index(self, directory="."):
        html = """<html><body><h2>TBFM:</h2>
        <a href="index?directory=%s">Up</a><br />
        """ % os.path.dirname(os.path.abspath(directory))

        for filename in glob.glob(directory + '/*'):
            absPath = os.path.abspath(filename)
            print (filename)
            if (not (os.path.isdir(absPath))) and (absPath.endswith('.mid')):
                # html += '<a href="' + filename + '">' + os.path.basename(filename) + "</a> <br />"
                html += '<a href="/download/?filepath=' + absPath + '">' + os.path.basename(filename) + "</a> <br />"

        html += """</body></html>"""
        return html
    index.exposed = True

class Download:

    def index(self, filepath):
        return serve_file(filepath, "application/x-download", "attachment")
    index.exposed = True

if __name__ == '__main__':
    root = Root()
    root.download = Download()
    cherrypy.quickstart(root, '/', "app.conf")