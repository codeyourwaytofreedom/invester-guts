from flask import Flask, render_template, request

invester = Flask(__name__)
invester.config["SECRET_KEY"] = "dtjdtjtkt4758"

@invester.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return render_template('wallets.html')
    return render_template("home.html")

if __name__ == "__main__":
    invester.run(debug=True)