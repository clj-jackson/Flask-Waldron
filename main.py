from flask import Flask, render_template, url_for
from forms import RegForm, LoginForm
app = Flask(__name__)
app.config["SECRET_KEY"] = "0bd24ce2ce9d0ac49fea3f26561cc7fa4fe296ef22964a68594b489c804d4f3a"

posts = [
    {
        "name": "Connor Jackson",
        "title": "Game post 0",
        "content": "This is some game dev stuff here",
        "date_posted": "22/06/21"
    },
{
        "name": "John Doe",
        "title": "Art post 0",
        "content": "This is some artsy stuff here",
        "date_posted": "25/06/21"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/opentabs")
def tabs():
    return render_template("tabs.html", title="Open Tabs")

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

@app.route("/register")
def register():
    form = RegForm()
    return render_template("register.html", title="Register", form=form)


if __name__ == "__main__":
    app.run(debug=True)