from bottle import Bottle,static_file,template,route,request,get,run
import bottle
import os
from zipfile import ZipFile
from paste import httpserver

UPLOAD_FOLDER = './upload'

def extrf(fname):
    with ZipFile(f"./upload/{fname}",'r') as zifi:
        zifi.extractall(path="./3d")

app = Bottle(__name__)

@app.route('/')
def root():
    return """
        <form action="/upload" method="post" enctype="multipart/form-data">
            Select a file: <input type="file" name="upload" />
            <input type="submit" value="Start upload" />
        </form>
    """ 

@app.route("/upload",method='POST')
def do_upload():
    f = request.files.get('upload')
    f.save(os.path.join(UPLOAD_FOLDER,f.filename))
    extrf(f.filename)
    os.remove(f"./upload/{f.filename}")
    return "uccessfully"

@app.get("/<filepath:re:.*\.(jpeg|png|gif|ico|svg|swf|jpg|cur)>")
@app.get("/<filepath:re:.*\.js>")
def staticf(filepath):
    response = static_file(filepath, root=f"3d/{name}")
    response.set_header("Cache-Control", "private, no-cache, no-store,")
    return response


@app.route('/<n>')
def index(n):
    global name
    name = n
    # return template(f'templates/3dv/{n}/index.htm')
    response = static_file('index.htm', root=f"3d/{name}")
    response.set_header("Cache-Control", "private, no-cache, no-store,")
    return response






application = bottle.default_app()
run(app=app,host="0.0.0.0",port=80,debug=True)