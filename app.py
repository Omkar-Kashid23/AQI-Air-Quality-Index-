from flask import Flask, jsonify, request, render_template
import requests
import os
app = Flask(__name__, static_folder='static', static_url_path='/static')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/api/air-quality', methods=['GET'])
def get_air_quality():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    print(f"Request received for lat={lat}, lon={lon}")
    if not lat or not lon:
        return jsonify({'error': 'Latitude and longitude are required'}), 400
    api_key = os.getenv('OPENWEATHER_API_KEY', " Enter your Api key here")
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        aqi = data['list'][0]['main']['aqi']
        pm10 = data['list'][0]['components'].get('pm10', 'N/A')
        pm25 = data['list'][0]['components'].get('pm2_5', 'N/A')
        result = {
            'aqi': aqi,
            'pm10': pm10,
            'pm25': pm25,
            'message': analyze_aqi(aqi),
            'coordinates': {'lat': lat, 'lon': lon}
        }
        response = jsonify(result)
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        return response
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API request failed: {str(e)}'}), 500
    except KeyError as e:
        return jsonify({'error': f'Missing key in API response: {str(e)}'}), 500
def analyze_aqi(aqi):
    messages = {
        1: "The air quality is good. No need to wear a mask.",
        2: "The air quality is fair. You may not need a mask, but it's advisable for sensitive people.",
        3: "The air quality is moderate. It's recommended to wear a mask for protection.",
        4: "The air quality is poor. It's advisable to wear a mask.",
        5: "The air quality is very poor. You must wear a mask."
    }
    return messages.get(aqi, "Could not determine the air quality.")
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
