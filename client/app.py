from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

model_url = 'http://127.0.0.1:60305/predict'

# Initialize Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    xml = request.data.decode()
    print(xml)
    soup = BeautifulSoup(xml, features="lxml")
    rows = soup.find_all('row')
    data = []
    for r in rows:
        data.append([
            float(r.sepal.width.string),
            float(r.sepal.height.string),
            float(r.petal.width.string),
            float(r.petal.height.string)
        ])
    print(data)
    res = requests.post(model_url, data=str(data))
    labels = res.json()
    preds = {}
    for i, r in enumerate(rows):
        preds[r.attrs['id']] = labels[i]
    return jsonify(preds)
    

@app.route('/')
def index():
    return """
    Hello! from IrisClassifier Client API
    Use /predict endpoint to get predict
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
