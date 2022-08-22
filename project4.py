from flask import Flask, render_template

invester = Flask(__name__)
invester.config["SECRET_KEY"] = "dtjdtjtkt4758"

@invester.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    invester.run(debug=True)