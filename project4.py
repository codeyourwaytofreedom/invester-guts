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


# api kullanım hakkı bitmesin
url = "https://v6.exchangerate-api.com/v6/569776aeffaab7cefabd8180/latest/TRY"
response = requests.get(url)
data = response.json()
rates = [float(str(1/data["conversion_rates"]["USD"]*1.015)[0:7]),
            float(str(1/data["conversion_rates"]["GBP"]*1.015)[0:7]),
            float(str(1/data["conversion_rates"]["EUR"]*1.015)[0:7])]
rates_sell = [float(str(1/data["conversion_rates"]["USD"])[0:7]),
            float(str(1/data["conversion_rates"]["GBP"])[0:7]),
            float(str(1/data["conversion_rates"]["EUR"])[0:7])]


@invester.route('/rates', methods = ['GET'])
def stuff():
    url = "https://v6.exchangerate-api.com/v6/569776aeffaab7cefabd8180/latest/TRY"
    response = requests.get(url)
    data = response.json()
    rates = [float(str(1/data["conversion_rates"]["USD"]*1.015)[0:7]),
            float(str(1/data["conversion_rates"]["GBP"]*1.015)[0:7]),
            float(str(1/data["conversion_rates"]["EUR"]*1.015)[0:7])]

    rates_sell = [str(1/data["conversion_rates"]["USD"])[0:7],
            str(1/data["conversion_rates"]["GBP"])[0:7],
            str(1/data["conversion_rates"]["EUR"])[0:7]]
    return jsonify(rate=rates, rates_sell=rates_sell)

@invester.route("/", methods=['POST', 'GET'])
def login():
    return  redirect(url_for('wallets'))

@invester.route("/create-wallet", methods=['POST', 'GET'])
def create_wallet():
    if request.method == 'POST':
        return redirect(url_for('wallets'))
    return render_template("create_wallet.html")

@invester.route("/wallets", methods= ["POST","GET"])
def wallets():
    wallet_ = wallet.query.get(1)
    if (request.method == "POST" and request.form.get("amount") and request.form.get("cbbuy")):
        add_to_balance = request.form.get("amount")
        print(add_to_balance)
        print(request.form.get("cbbuy"))
        currency_selected = request.form.get("select")
        if currency_selected=="1":
            if float(request.form.get("amount"))*rates[0] > wallet.query.get(1).balance:
                flash("Not enough balance!!!", "error")
            else:
                wallet.query.get(1).usd_bal=float(request.form.get("amount"))+wallet.query.get(1).usd_bal
                wallet.query.get(1).balance = str(wallet.query.get(1).balance - float(request.form.get("amount"))*rates[0])[0:9]
                db.session.commit()
                flash ("Purchase successful: +" +request.form.get("amount") + " USD", "success")
        elif currency_selected=="2":
            if float(request.form.get("amount"))*rates[1] > wallet.query.get(1).balance:
                flash("Not enough balance!!!", "error")
            else:
                wallet.query.get(1).eur_bal=float(request.form.get("amount"))+wallet.query.get(1).eur_bal
                wallet.query.get(1).balance = str(wallet.query.get(1).balance - float(request.form.get("amount"))*rates[1])[0:9]
                db.session.commit()
                flash ("Purchase successful: +" +request.form.get("amount") + " EUR", "success")
        elif currency_selected=="3":
            if float(request.form.get("amount"))*rates[2] > wallet.query.get(1).balance:
                flash("Not enough balance!!!", "error")
            else:
                wallet.query.get(1).gbp_bal=float(request.form.get("amount"))+wallet.query.get(1).gbp_bal
                wallet.query.get(1).balance = str(wallet.query.get(1).balance - float(request.form.get("amount"))*rates[2])[0:9]
                db.session.commit()
                flash ("Purchase successful: +" +request.form.get("amount") + " GBP", "success")
        
        print(wallet.query.get(1))

        return redirect(url_for("wallets"))

    elif (request.method == "POST" and request.form.get("amount") and request.form.get("cbsell")):
        add_to_balance = request.form.get("amount")
        print(add_to_balance)
        print(request.form.get("cbsell"))
        currency_selected = request.form.get("select")
        if currency_selected=="1":
            if float(request.form.get("amount")) > wallet.query.get(1).usd_bal:
                flash("Not enough balance!!!", "error")
            else:
                wallet.query.get(1).usd_bal=wallet.query.get(1).usd_bal - float(request.form.get("amount"))
                wallet.query.get(1).balance = str(wallet.query.get(1).balance + float(request.form.get("amount"))*rates_sell[0])[0:9]
                db.session.commit()
                flash ("Sale successful: -" +request.form.get("amount") + " USD", "success")
        elif currency_selected=="2":
            if float(request.form.get("amount")) > wallet.query.get(1).eur_bal:
                flash("Not enough balance!!!", "error")
            else:
                wallet.query.get(1).eur_bal= wallet.query.get(1).eur_bal - float(request.form.get("amount"))
                wallet.query.get(1).balance = str(wallet.query.get(1).balance + float(request.form.get("amount"))*rates_sell[1])[0:9]
                db.session.commit()
                flash ("Sale successful: -" +request.form.get("amount") + " EUR", "success")
        elif currency_selected=="3":
            if float(request.form.get("amount")) > wallet.query.get(1).gbp_bal:
                flash("Not enough balance!!!", "error")
            else:
                wallet.query.get(1).gbp_bal= wallet.query.get(1).gbp_bal - float(request.form.get("amount"))
                wallet.query.get(1).balance = str(wallet.query.get(1).balance + float(request.form.get("amount"))*rates_sell[2])[0:9]
                db.session.commit()
                flash ("Sale successful: -" +request.form.get("amount") + " GBP", "success")
        
        print(wallet.query.get(1))

        return redirect(url_for("wallets"))
        
    else:
        return render_template('wallets.html', budget=wallet_, rates=rates, rates_sell=rates_sell)
    






if __name__ == "__main__":
    invester.run(debug=True)
