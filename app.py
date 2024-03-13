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
    is_uploaded = upload_file_to_s3(username)
    if is_uploaded is not None:
        os.remove(file_path)
    return render_template('index.html', upload_status="File uploaded successfully. Generating BDD scenario...")
    # return redirect('/generate-bdd')


@app.route("/generate-bdd")
def generate_bdd():
    username = session['username']
    url = generate_bdd_scenario(username)
    if url is None:
        return render_template('index.html', status="Failed to generate BDD scenario")
    return render_template('index.html', status="Bdd generated successfully", response=url)


@app.route("/generate_test", methods=['POST'])
def generate_test():
    lob = request.form.get('lob')
    state = request.form.get('state')
    test_cases = request.form.get('test_cases')
    url = generate_test_data(lob, state, test_cases)
    if url is None:
        return render_template('index.html', status="Failed to generate test data")
    return render_template('index.html', status="Test data generated successfully", response=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
