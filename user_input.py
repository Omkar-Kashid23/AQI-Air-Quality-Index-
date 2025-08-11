imort requests
api_key = ""  # Replace with your API key
city = 'Pune'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
response.raise_for_status()  # Raise an exception for error status codes
data = response.json()
