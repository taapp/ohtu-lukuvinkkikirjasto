from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from functools import wraps
from entities.lukuvinkki import Lukuvinkki
from entities.lukuvinkkilista import Lukuvinkkilista
from entities.users import Users
from services.vinkki_service import vinkki_service
#lisätty user importti
from entities.user import User


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
    user_entry = Users.get(username)
    if (user_entry is not None):
        user = Users(user_entry[0],user_entry[0],user_entry[1])
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
    if (user.get_password(username) == password):
        login_user(user)
        vinkki_service._user = current_user
        return render_list()
    elif (user.get_password(username) != password):
        return render_template("login.html", error = "Väärä tunnus tai salasana!")

@app.route("/list", methods=["GET", "POST"])
@login_required
def render_list():
    #return render_template("list.html", lista=vinkki_service.palauta_lista())
    return render_template("list.html", lista=vinkki_service.palauta_lista_user_current())

@app.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")

@app.route("/add_subject", methods=["GET"])
@login_required
def render_add_subject():
    return render_template("add_subject.html")

#ei vielä toimi, puuttuu vinkin spesifiointi
@app.route("/modify_subject/<subject_name>", methods=["GET"])
@login_required
def render_modify_subject(otsikko):
    #palauta vinkki tähän (servicessä ei vielä metodia hakuun!)
    #vinkin attribuutit sitten parametrina html-näkymään
    return render_template("modify_subject.html", subject_name = otsikko)

@app.route("/register", methods=["POST"])
def handle_register():
    print("kutsutaan handle_register")
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirmation = request.form.get("password_confirmation")
    # lisätty rekisteröinnin yritys
    vinkki_service.add_user_to_userlist(vinkki_service.create_user(username, password))
    return redirect_to_home()
    #try:
    #    vinkki_service.add_user_to_userlist(vinkki_service.create_user(username, password))
    #    return redirect_to_home()
    #except Exception as error:
    #    flash(str(error))
    #    return redirect_to_home()

@app.route("/logout")
def logout():
    logout_user()
    return redirect_to_home()

@app.route("/add_subject", methods=["GET", "POST"])
@login_required
def add_subject():
    print("kutsutaan add_subject")
    print(current_user)
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
        vinkki_service.add_vinkki_to_vinkkilista(vinkki_service.create_vinkki(tyyppi, otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit))
        return render_list()
    except Exception as error:
        flash(str(error))
        return redirect_to_home()

#ei vielä toiminnassa! odottaa hakumetodia
@app.route("/modify_subject/<subject_name>", methods=["GET", "POST"])
@login_required
def modify_subject():
    otsikko = request.form.get("otsikko")
    kirjailija = request.form.get("kirjailija")
    isbn = request.form.get("isbn")
    tagit = request.form.get("tagit")
    url = request.form.get("url")
    kommentti = request.form.get("kommentti")
    kuvaus = request.form.get("kuvaus")
    kurssit = request.form.get("kurssit")
    try:
        vinkki_service.muokkaa_vinkkia(otsikko, kirjailija, isbn, tagit, url, kommentti, kuvaus, kurssit)
        return render_list()
    except Exception as error:
        flash(str(error))
        return redirect_to_home()