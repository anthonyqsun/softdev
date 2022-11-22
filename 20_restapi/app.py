from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    with open('key_nasa.txt', 'r+') as f:
        key = f.read()
        response = requests.get('https://api.nasa.gov/planetary/earth/assets?lon=100.75&lat=1.5&date=2014-02-01&dim=0.15&api_key=' + key)
        data = response.json()
        return render_template('main.html', data=data['url'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="5001")
