from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

def get_aqi_bucket(aqi):
    if aqi >= 0 and aqi <= 50:
        return "Good"
    elif aqi > 50 and aqi <= 100:
        return "Satisfactory"
    elif aqi > 100 and aqi <= 200:
        return "Moderate"
    elif aqi > 200 and aqi <= 300:
        return "Poor"
    elif aqi > 300 and aqi <= 400:
        return "Very Poor"
    elif aqi > 400:
        return "Severe"
    else:
        return "Invalid AQI value"

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def predict():
    PM2 = float(request.form['PM2.5'])
    PM10 = float(request.form['PM10'])
    NO = float(request.form['NO'])
    NO2 = float(request.form['NO2'])
    NOx = float(request.form['NOx'])
    NH3 = float(request.form['NH3'])
    CO = float(request.form['CO'])
    SO2 = float(request.form['SO2'])
    O3 = float(request.form['O3'])
    
    output = model.predict([[PM2, PM10, NO, NO2, NOx, NH3, CO, SO2, O3]])[0]
    output=round(output,2)
    category = get_aqi_bucket(output)
    
    return render_template('result.html', prediction_text="PREDICTED AQI IS {} - AQI Category: {}".format(output, category))

@app.route('/eda')
def eda():
    return render_template('eda.html')

@app.route('/git')
def git():
    return render_template('github.html')
@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(port=14000)
