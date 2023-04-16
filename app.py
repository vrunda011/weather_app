import requests
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/weather")
def weather():
    url = 'http://api.weatherapi.com/v1/current.json'
    key = '4d97521ec9d3488d90281006231504'
    q = 'vadodara'
    response = requests.get("%s?key=%s&q=%s"%(url, key, q))
    response = response.json()
    temp = str(response['current']['temp_c'])
    current_time = datetime.now().strftime("%B %d, %Y")
    return render_template("weather.html",date=current_time,city='vadodara',temp=temp)


if __name__ == "__main__":
    app.run(debug=True, port=8080)

