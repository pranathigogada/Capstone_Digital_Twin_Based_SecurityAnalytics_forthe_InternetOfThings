from flask import Flask, request, jsonify, render_template
import pickle
import datetime
import pandas as pd

app = Flask(__name__)

# Load the models
with open('weathertype.pkl', 'rb') as file:
    model1 = pickle.load(file)

with open('thermostattype.pkl', 'rb') as file:
    model2 = pickle.load(file)

with open('fridgetype.pkl', 'rb') as file:
    model3 = pickle.load(file)

def predict_weather(features_df):
    # Make predictions using the models
    prediction_encoded_weather = model1.predict(features_df)
    prediction_encoded_thermostat = model2.predict(features_df)
    prediction_encoded_fridge = model3.predict(features_df)
    
    # Mapping encoded values to types
    types = {0: 'ddos', 1: 'xss', 2: 'backdoor', 3: 'injection', 4: 'normal', 5: 'password', 6: 'ransomware', 7: 'scanning'}
    weather_type = types[prediction_encoded_weather[0]]
    thermostat_type = types[prediction_encoded_thermostat[0]]
    fridge_type = types[prediction_encoded_fridge[0]]

    return {'weather_type': weather_type, 'thermostat_type': thermostat_type, 'fridge_type': fridge_type}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from the form
    month = int(request.form['month'])
    day = int(request.form['day'])
    hour = int(request.form['hour'])
    minute = int(request.form['minute'])

    # Create a DataFrame with the features
    features_df = pd.DataFrame({
        'month': [month],
        'day': [day],
        'hour': [hour],
        'minute': [minute]
    })

    # Get the prediction
    result = predict_weather(features_df)

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
