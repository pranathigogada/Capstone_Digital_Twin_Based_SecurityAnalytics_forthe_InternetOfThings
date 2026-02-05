from flask import Flask, request, jsonify
import pickle
import datetime
import pandas as pd

app = Flask(__name__)

# Load the model
with open('weathertype.pkl', 'rb') as file:
    model1 = pickle.load(file)

# Load the model
with open('thermostattype.pkl', 'rb') as file:
    model2 = pickle.load(file)

# Load the model
with open('fridgetype.pkl', 'rb') as file:
    model3 = pickle.load(file)

@app.route('/predict_weather', methods=['POST'])
def predict_weather():
    # Extract date and time from the request
    data = request.get_json()
    system_datetime = data['datetime']  # expecting datetime in ISO format

    # Convert string datetime to datetime object
    dt = datetime.datetime.fromisoformat(system_datetime)

    # Create a DataFrame with the necessary features
    features_df = pd.DataFrame({
        'month': [dt.month],
        'day': [dt.day],
        'hour': [dt.hour],

        'minute': [dt.minute]
    })

    # Make a prediction using the model
    prediction_encoded_weather = model1.predict(features_df)
    prediction_encoded_thermostat = model2.predict(features_df)
    prediction_encoded_fridge = model3.predict(features_df)
    
    # Assuming the weather types are encoded and you have the encoder
    # You need to save and load the encoder just like the model if necessary
    # weather_type = label_encoder.inverse_transform(prediction_encoded)[0]

    # For demonstration, let's assume the labels are numbers representing weather types:
    # 0: Sunny, 1: Rainy, 2: Cloudy, etc. (Adjust according to actual encoding)
    types = {0: 'ddos', 1: 'xss', 2: 'backdoor',3: 'injection', 4: 'normal',5 : 'password',6:'ransomware',7:'scanning'}
    weather_type = types[prediction_encoded_weather[0]]
    thermostat_type = types[prediction_encoded_thermostat[0]]
    fridge_type = types[prediction_encoded_fridge[0]]

    # Return the prediction
    print(weather_type)
    return jsonify({'weather_type': weather_type, 'thermostat_type':thermostat_type, 'fridge_type':fridge_type })

if __name__ == '__main__':
    app.run(debug=True)

