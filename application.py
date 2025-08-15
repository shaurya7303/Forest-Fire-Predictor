import pickle 
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

template_dir = os.path.abspath('C:\\Users\\Dell\\rlr\\template')
application = Flask(__name__, template_folder=template_dir)

app=application

# Load the pre-trained model
linear_model = pickle.load(open('models/linear.pkl', 'rb'))
std_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temprature=float(request.form.get('Temprature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))        
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))

        newscaled_data=std_scaler.transform([[Temprature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=linear_model.predict(newscaled_data)

        return render_template('home.html', results=(result[0]))



    else:
        return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')