import flask as fl

app = fl.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return fl.render_template('home.html')





@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    return fl.redirect(fl.url_for("home"))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if fl.request.method == 'POST':
        return fl.do_the_login()
    else:
        return fl.show_the_login_form()


if __name__ == "__main__":
    app.run()
