from flask import Flask, render_template, url_for
app = Flask(__name__)

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
    return render_template("login.html", title="Login")

if __name__ == "__main__":
    app.run(debug=True)