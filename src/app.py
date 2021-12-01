from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

def redirect_to_login():
    return redirect(url_for("render_login"))

def redirect_to_register():
    return redirect(url_for("render_register"))

@app.route("/")
def render_home():
    return render_template("index.html")

@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")