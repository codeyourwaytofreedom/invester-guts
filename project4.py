from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import requests
from flask_sqlalchemy import SQLAlchemy


invester = Flask(__name__)
invester.config["SECRET_KEY"] = "dtjdtjtkt4758"
invester.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wallets.db'

db = SQLAlchemy(invester)

class wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, nullable=False)
    usd_bal = db.Column(db.Integer, nullable=False)
    eur_bal = db.Column(db.Integer, nullable=False)
    gbp_bal = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Company('{self.id}','{self.balance}','{self.usd_bal}', '{self.eur_bal}', '{self.gbp_bal}')"



url = "https://v6.exchangerate-api.com/v6/569776aeffaab7cefabd8180/latest/TRY"
response = requests.get(url)
data = response.json()

print("rates loaded")

@invester.route("/", methods=['POST', 'GET'])
def login():
    return  redirect(url_for('create_wallet'))

@invester.route("/create-wallet", methods=['POST', 'GET'])
def create_wallet():
    if request.method == 'POST':
        return redirect(url_for('wallets'))
    return render_template("create_wallet.html")

@invester.route("/wallets", methods= ["POST","GET"])
def wallets():
    wallet_ = wallet.query.get(1)
    if (request.method == "POST" and request.form.get("amount")):
        add_to_balance = request.form.get("amount")
        print(add_to_balance)
        currency_selected = request.form.get("select")
        if currency_selected=="1":
            wallet.query.get(1).usd_bal=float(request.form.get("amount"))+wallet.query.get(1).usd_bal
            wallet.query.get(1).balance = str(wallet.query.get(1).balance - float(request.form.get("amount"))*1/data["conversion_rates"]["USD"])[0:9]
            db.session.commit()
            c = "USD"
        elif currency_selected=="2":
            wallet.query.get(1).eur_bal=float(request.form.get("amount"))+wallet.query.get(1).eur_bal
            wallet.query.get(1).balance = str(wallet.query.get(1).balance - float(request.form.get("amount"))*1/data["conversion_rates"]["EUR"])[0:9]
            db.session.commit()
            c = "EUR"
        elif currency_selected=="3":
            wallet.query.get(1).gbp_bal=float(request.form.get("amount"))+wallet.query.get(1).gbp_bal
            wallet.query.get(1).balance = str(wallet.query.get(1).balance - float(request.form.get("amount"))*1/data["conversion_rates"]["GBP"])[0:9]
            db.session.commit()
            c = "GBP"
        flash ("You have bought " +request.form.get("amount") + " "+ c)
        print(wallet.query.get(1))

        return redirect(url_for("wallets"))
        
    else:
        return render_template('wallets.html', budget=wallet_)
    

@invester.route('/rates', methods = ['GET'])
def stuff():
    # print(1/data["conversion_rates"]["USD"])
    # print(1/data["conversion_rates"]["GBP"])
    # print(1/data["conversion_rates"]["EUR"])
    rates = [str(1/data["conversion_rates"]["USD"])[0:7],
            str(1/data["conversion_rates"]["GBP"])[0:7],
            str(1/data["conversion_rates"]["EUR"])[0:7]]
    return jsonify(rate=rates)




if __name__ == "__main__":
    invester.run(debug=True)
