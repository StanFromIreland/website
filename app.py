import flask
from flask import render_template

app = flask.Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/projects/")
def projects():
    return render_template('projects.html')

@app.route("/projects/website/")
def projects_website():
    return render_template('website.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
