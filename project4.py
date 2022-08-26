from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests



invester = Flask(__name__)
invester.config["SECRET_KEY"] = "dtjdtjtkt4758"


@invester.route("/", methods=['POST', 'GET'])
def login():
    return  redirect(url_for('create_wallet'))

@invester.route("/create-wallet", methods=['POST', 'GET'])
def create_wallet():
    if request.method == 'POST':
        return redirect(url_for('wallets'))
    return render_template("create_wallet.html")

@invester.route("/wallets")
def wallets():
    return render_template('wallets.html')


@invester.route('/rates', methods = ['GET'])
def stuff():
    url = "https://v6.exchangerate-api.com/v6/569776aeffaab7cefabd8180/latest/TRY"
    response = requests.get(url)
    data = response.json()

    print(1/data["conversion_rates"]["USD"])
    print(1/data["conversion_rates"]["GBP"])
    print(1/data["conversion_rates"]["EUR"])
    rates = [str(1/data["conversion_rates"]["USD"])[0:7],
            str(1/data["conversion_rates"]["GBP"])[0:7],
            str(1/data["conversion_rates"]["EUR"])[0:7]]
    return jsonify(rate=rates)




if __name__ == "__main__":
    invester.run(debug=True)
