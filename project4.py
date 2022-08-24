from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
import datetime

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
    tim=datetime.datetime.today()
    print(tim)
    return render_template('wallets.html', tim=tim)

def get_price():
    url = "http://api.coincap.io/v2/assets?"
    response = requests.request("GET", url, headers={}, data = {})
    if response.status_code == 200:
        data=response.json()['data'][0]['priceUsd']
        print(data)
        return data
    else:
        print("Error")  
        return 0


@invester.route('/Crypto_Price', methods = ['GET'])
def stuff():
    price=get_price()
    return jsonify(result=price)

@invester.route('/test')
def index():
    return render_template('test.html')


if __name__ == "__main__":
    invester.run(debug=True)