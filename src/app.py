from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from functools import wraps
from services.vinkki_service import vinkki_service
from repositories.user_repository import user_repository

app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['TESTING'] = False

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


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

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

@app.route("/", methods=["GET", "POST"])
def render_home():
    return render_template("index.html")

@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")

@login_manager.user_loader
def load_user(username):
    user = vinkki_service.get_user(username)
    if (user is not None):
        return user
    return None

@app.route("/login", methods = ["GET", "POST"])
def login():
    print("kutsutaan login")
    username = request.form.get("username")
    password = request.form.get("password")
    user = load_user(username)

    if not user:
        return render_template("login.html", error = "Väärä tunnus tai salasana!")
    if (user.get_password() == password):
        login_user(user)
        vinkki_service._user = current_user
        return render_list()
    elif (user.get_password() != password):
        return render_template("login.html", error = "Väärä tunnus tai salasana!")

@app.route("/list", methods=["GET", "POST"])
@login_required
def render_list():
    return render_template("list.html", lista=vinkki_service.palauta_lista_user_current())

@app.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")

@app.route("/add_subject", methods=["GET"])
@login_required
def render_add_subject():
    return render_template("add_subject.html")

#ei vielä toimi, puuttuu vinkin spesifiointi
@app.route("/modify_subject<subject_name>", methods=["GET"])
@login_required
def render_modify_subject(subject_name):
    vinkki = vinkki_service.palauta_vinkki(subject_name)[0]
    return render_template("modify_subject.html", otsikko = vinkki.palauta_otsikko(), 
        kirjailija = vinkki.palauta_kirjailija(), 
        isbn = vinkki.palauta_isbn(), 
        tagit = vinkki.palauta_tagit(), 
        url = vinkki.palauta_url(), 
        kommentti = vinkki.palauta_kommentti(), 
        kuvaus = vinkki.palauta_kuvaus(), 
        kurssit = vinkki.palauta_kurssit())

@app.route("/register", methods=["POST"])
def handle_register():
    print("kutsutaan handle_register")
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirmation = request.form.get("password_confirmation")
    
    check_if_user = user_repository.find_username(username)

    if check_if_user is not None:
        return render_template("register.html", error = "Tunnus on jo käytössä")
    
    if password != password_confirmation:
        return render_template("register.html", error = "Salasanat eivät täsmää")
    
    if not (username and password and password_confirmation):
        return render_template("register.html", error = "Kaikki kentät on täytettävä")
    
    if len(password) < 4:
        return render_template("register.html", error = "Salasanan pitää olla vähintään 5 merkkiä pitkä")

    if len(username) < 3:
        return render_template("register.html", error = "Käyttäjätunnuksen pitää olla vähintään 3 merkkiä pitkä")
        
    
    vinkki_service.add_user_to_userlist(vinkki_service.create_user(username, password))
    
    return redirect_to_home()

@app.route("/logout")
def logout():
    logout_user()
    return redirect_to_home()

@app.route("/add_subject", methods=["GET", "POST"])
@login_required
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
    yksityinen = request.form.get("yksityinen")
    username = current_user.username if yksityinen is not None else None
    try:
        vinkki_service.add_vinkki_to_vinkkilista(vinkki_service.create_vinkki(tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit, username=username))
        return render_list()
    except Exception as error:
        flash(str(error))
        return redirect_to_home()

#ei vielä toiminnassa! odottaa hakumetodia
@app.route("/modify_subject<subject_name>", methods=["GET", "POST"])
@login_required
def modify_subject(subject_name):
    vanhaotsikko = subject_name
    otsikko = request.form.get("otsikko")
    kirjailija = request.form.get("kirjailija")
    isbn = request.form.get("isbn")
    tagit = request.form.get("tagit")
    url = request.form.get("url")
    kommentti = request.form.get("kommentti")
    kuvaus = request.form.get("kuvaus")
    kurssit = request.form.get("kurssit")
    try:
        vinkki_service.muokkaa_vinkkia(vanhaotsikko, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit)
        return render_list()
    except Exception as error:
        flash(str(error))
        return redirect_to_home()

@app.route("/search", methods=["GET", "POST"])
@login_required
def render_search():
    searchword = request.form.get("word")
    return render_template("list.html", lista=vinkki_service.hae_vinkkia(searchword))