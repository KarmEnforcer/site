from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)




@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/education")
def education():
    return render_template('education.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')


@app.route("/skills")
def skills():
    return render_template('skills.html')


@app.route("/projects")
def projects():
    return render_template('projects.html')






if __name__ == "__main__":
    app.run(debug=True)
