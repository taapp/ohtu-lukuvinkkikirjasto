from flask import Flask, render_template, redirect, url_for, request, flash
from entities.lukuvinkki import Lukuvinkki
from entities.lukuvinkkilista import Lukuvinkkilista

app = Flask(__name__)

lukuvinkkilista = Lukuvinkkilista()

def redirect_to_login():
    return redirect(url_for("render_login"))

def redirect_to_register():
    return redirect(url_for("render_register"))

def redirect_to_add_subject():
    return redirect(url_for("render_add_subject"))

def redirect_to_home():
    return redirect(url_for("render_home"))

def redirect_to_list():
    return redirect(url_for("render_list"))

@app.route("/", methods=["GET", "POST"])
def render_home():
    return render_template("index.html")

@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")

@app.route("/list", methods=["GET", "POST"])
def render_list():
    return render_template("list.html", lukuvinkkilista=lukuvinkkilista)

@app.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")

@app.route("/add_subject", methods=["GET"])
def render_add_subject():
    return render_template("add_subject.html")

@app.route("/register", methods=["POST"])
def handle_register():
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirmation = request.form.get("password_confirmation")

@app.route("/add_subject", methods=["POST"])
def add_subject():
    tyyppi = request.form.get("tyyppi")
    otsikko = request.form.get("otsikko")
    kirjailija = request.form.get("kirjailija")
    isbn = request.form.get("isbn")
    tagit = request.form.get("tagit")
    url = request.form.get("url")
    kommentti = request.form.get("kommentti")
    kuvaus = request.form.get("kuvaus")
    kurssit = request.form.get("kurssit")

    try:
        lukuvinkkilista.lisaa(Lukuvinkki(tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit))
        return redirect_to_list()
    except Exception as error:
        flash(str(error))
        return redirect_to_register()
