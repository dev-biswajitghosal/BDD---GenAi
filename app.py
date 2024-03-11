import os
import uuid

from flask import Flask, render_template, request, redirect, session
from aws_s3 import generate_bdd_scenario, generate_test_data , upload_file_to_s3

app = Flask(__name__)
app.secret_key = os.urandom(24)

UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/generate-bdd")
def generate_bdd():
    username = session['username']
    url = generate_bdd_scenario(username)
    if url is None:
        return render_template('index.html', status="Failed to generate BDD scenario")
    return render_template('index.html', status="Bdd generated successfully", response=url)


@app.route("/generate_test")
def generate_test():
    username = session['username']
    lob = request.args.get('lob')
    state = request.args.get('state')
    test_cases = request.args.get('test_cases')
    url = generate_test_data(username, lob, state, test_cases)
    if url is None:
        return render_template('index.html', status="Failed to generate test data")
    return render_template('index.html', status="Test data generated successfully", response=url)


@app.route("/upload-bdd", methods=['POST'])
def upload_bdd():
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
    return redirect('/generate-bdd')


@app.route("/upload-test", methods=['POST'])
def upload_test():
    if 'username' not in session:
        session['username'] = str(uuid.uuid4())
    username = session['username']
    lob = request.args.get('lob')
    state = request.args.get('state')
    test_cases = request.args.get('test_cases')
    print(f"LOB: {lob}, State: {state}, Test Cases: {test_cases},username: {username}")
    return redirect('/generate_test')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
