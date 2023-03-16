from bottle import Bottle,static_file,template,route,request,get,run
import os
from zipfile import ZipFile

UPLOAD_FOLDER = './upload'

def extrf(fname):
    with ZipFile(f"./upload/{fname}",'r') as zifi:
        zifi.extractall(path="./templates/3dv")
    
app = Bottle(__name__)

@app.route('/')
def root():
    return static_file('index.html', root='templates/site')


@app.route('/upload', method='POST')
def do_upload():
    f = request.files.get('upload')
    f.save(os.path.join(UPLOAD_FOLDER,f.filename))
    extrf(f.filename)
    os.remove(f"./upload/{f.filename}")
    return static_file('index2.html', root='templates/site')




@app.get("/<filepath:re:.*\.(jpeg|png|gif|ico|svg|swf|jpg|cur)>")
@app.get("/<filepath:re:.*\.js>")
def staticf(filepath):
    response = static_file(filepath, root=f"templates/3dv/{name}")
    response.set_header("Cache-Control", "private, no-cache, no-store,")
    return response


# @app.get("/<filepath:re:.*\.(jpeg|png|gif|ico|svg)>")
# def img(filepath):
#     return static_file(filepath, root=f"templates/3dv/{name}")

@app.route('/<n>')
def index(n):
    global name
    name = n
    # return template(f'templates/3dv/{n}/index.htm')
    response = static_file('index.htm', root=f"templates/3dv/{name}")
    response.set_header("Cache-Control", "private, no-cache, no-store,")
    return response



run(app=app,host='0.0.0.0', port=80, debug=True)