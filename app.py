from flask import Flask, request, render_template, Response
UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)

# Get info via params
@app.route('/users', methods=['GET'])
def hello():
    name = request.args.get("name")
    appName = request.args.get("appName")
    return f'Hello {name}, welcome to {appName}!'


# Post info and return interpolated strings
@app.route('/users', methods=['POST'])
def goodbye():
    name = request.args.get("name")
    appName = request.args.get("appName")
    return f'Thank you for posting on {appName}, {name}!'

# Upload a file and return the content
@app.route("/", methods=["GET", "POST"]) 
def index(): 
    if request.method == "POST": 
        file = request.files.get("file") 
        file_content = file.read() 

        if file_content:
            return Response(file_content, mimetype="text/plain")
        else: 
            return  Response(status=400, response="Bad Request" ,mimetype="text/plain")
            
    return render_template("index.html") 
