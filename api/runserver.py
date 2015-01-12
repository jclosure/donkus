"""
This script runs the web application using a development server.
"""
import os
from os import *
import pathlib
from os import environ
from eve import Eve

app = Eve()

if __name__ == '__main__':

    # Setup the host url and port
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5555
 
    # Setup extra_files to watch - http://stackoverflow.com/questions/9508667/reload-flask-app-when-template-file-changes
    extra_dirs = ['donkus', 'web']
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)

    # Start with watching the extra files and reloading enabled
    app.run(HOST, PORT, extra_files=extra_files, debug=True)

    # Start without for Visual Studio debugger to work on static py files at build time
    #app.run(HOST, PORT)