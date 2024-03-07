import os
import uuid

from flask import Flask, render_template, request, redirect, session
from aws_s3 import generate_bdd_scenario, upload_file_to_s3

app = Flask(__name__)
app.secret_key = os.urandom(24)

UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/response")
def response():
    username = session['username']
    url = generate_bdd_scenario(username)
    # print("Output File: "+url)
    return render_template('index.html', response=url)


@app.route("/upload", methods=['POST'])
def upload():
    if 'username' not in session:
        session['username'] = str(uuid.uuid4())
    username = session['username']
    file = request.files['file']
    # print('FileName= ' + file.filename)
    file_path = UPLOAD_FOLDER + f"/{username}_input.xlsx"
    if os.path.exists(file_path):
        os.remove(file_path)
    file.save(file_path)
    upload_file_to_s3(username)
    return redirect('/response')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
