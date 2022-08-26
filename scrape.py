import requests

url = "https://v6.exchangerate-api.com/v6/569776aeffaab7cefabd8180/latest/TRY"
response = requests.get(url)
data = response.json()

print(1/data["conversion_rates"]["USD"])
print(1/data["conversion_rates"]["GBP"])
print(1/data["conversion_rates"]["EUR"])
