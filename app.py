import os
import uuid

from flask import Flask, render_template, request, redirect, session
from aws_s3 import generate_bdd_from_jira, generate_bdd_scenario, generate_test_data, upload_file_to_s3
from jira import get_issues

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


@app.route("/generate_bdd_jira", methods=['POST'])
def generate_bdd_jira():
    try:
        jira_url = request.form.get('jira_url')
        email = request.form.get('email')
        password = request.form.get('password')
        board_id = request.form.get('board_id')
        sprint_id = request.form.get('sprint_id')
        user_story = get_issues(jira_url=jira_url, email=email, password=password, board_id=board_id, sprint_id=sprint_id)
        if len(user_story) == 0:
            return render_template('index.html', status="No active user stories found")
        url = generate_bdd_from_jira(user_story)
        if url is None:
            return render_template('index.html', status="Failed to generate BDD scenario")
        return render_template('index.html', status="Bdd generated successfully", response=url)
    except:
        return render_template('index.html', status="Provide correct details")


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
