from flask import (
    render_template,
    flash,
    redirect,
    request,
    url_for,
    make_response,
    session,
)
from app import app
from app.forms import LoginForm, cookieSubmitForm


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    user = {"username": "Joseph"}
    if "USERCOOKIE" not in session:
        session["USERCOOKIE"] = ""
    print(session["USERCOOKIE"])
    return render_template("index.html", title="Home", user=user)


@app.route("/cookies", methods=["GET", "POST"])
def set_cookies():
    form = cookieSubmitForm()
    print(session)
    if request.method == "POST":
        cookie_text = request.form["cookie_text"]
        session["USERCOOKIE"] = cookie_text
        # flash("You entered: {}".format(cookie_text))
        # resp = make_response(
        #     render_template("set_cookie.html", title="Cookie Test", form=form)
        # )
        # resp.set_cookie("usercookie", cookie_text)
        return redirect(url_for("set_cookies"))
    return render_template("set_cookie.html", title="Cookie Test", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
