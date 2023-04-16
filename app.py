import requests
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/weather")
def weather():
    url = 'http://api.weatherapi.com/v1/current.json'
    key = '4d97521ec9d3488d90281006231504'
    q = request.args.get('city', 'vadodara')
    response = requests.get("%s?key=%s&q=%s"%(url, key, q))
    response = response.json()

    current_time = datetime.now().strftime("%B %d, %Y")

    if 'error' in response:
        return render_template("weather.html",date=current_time,city='City not found',temp=0)

    temp = str(response['current']['temp_c'])
    return render_template("weather.html",date=current_time,city=q,temp=temp)


if __name__ == "__main__":
    app.run(debug=True, port=8080)

