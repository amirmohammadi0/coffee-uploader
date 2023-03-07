from bottle import *
import os
from zipfile import ZipFile

UPLOAD_FOLDER = './upload'

def extrf(fname):
    with ZipFile(f"./upload/{fname}",'r') as zifi:
        zifi.extractall(path="./templates/3dv")
    



@route('/')
def root():
    return static_file('index.html', root='templates/site')



@route('/upload', method='POST')
def do_upload():
    f = request.files.get('upload')
    f.save(os.path.join(UPLOAD_FOLDER,f.filename))
    extrf(f.filename)
    os.remove(f"./upload/{f.filename}")
    return static_file('index.html', root='templates/site')



@get("/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root=f"templates/3dv/{name}")


@get("/<filepath:re:.*\.(jpeg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root=f"templates/3dv/{name}")

@route('/<n>')
def index(n):
    global name
    name = n
    return template(f'templates/3dv/{n}/index.htm')


run(host='localhost', port=8080,debug=True)