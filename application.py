# app.py
from flask import Flask, redirect, url_for, render_template, request
from insurance.logger import logging
from insurance.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

@application.route('/')
def welcome():
    return render_template('index.html')

@application.route('/success/<int:score>')
def success(score):
    return render_template('result.html', result=score)

@application.route('/submit', methods=['POST', 'GET'])
def submit():
    predicted_value = 0
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = request.form['sex']
        bmi = float(request.form['bmi'])
        children = float(request.form['children'])
        smoker = request.form['smoker']
        region = request.form['region']
        print('data captured:', age, sex, bmi, children, smoker, region)
        features = CustomData(age=age, sex=sex, bmi=bmi, children=children, smoker=smoker, region=region).get_data_as_data_frame()
        predicted_value = PredictPipeline().predict(features)

    return render_template('result.html', result=predicted_value[0])

if __name__ == '__main__':
    application.run(host='0.0.0.0')
