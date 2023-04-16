import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/weather")
def weather():
    response = requests.get("http://api.weatherapi.com/v1/current.json?key=4d97521ec9d3488d90281006231504&q=vadodara")
    response = response.json()
    return "<div style='color:red'>Weather of vadodara : "+str(response['current']['temp_c']) + "</div>"
    
    


if __name__ == "__main__":
    app.run(debug=True, port=8080)

