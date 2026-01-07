<<<<<<< HEAD
import requests

def get_weather(city):
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en"
    geo_response = requests.get(geocode_url)
    
    if geo_response.status_code != 200 or not geo_response.json().get("results"):
        print("City not found. Please check the spelling and try again.")
        return
    
    lat = geo_response.json()["results"][0]["latitude"]
    lon = geo_response.json()["results"][0]["longitude"]
    location_name = geo_response.json()["results"][0]["name"]
    country = geo_response.json()["results"][0].get("country", "")
    
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,apparent_temperature,weather_code,wind_speed_10m,relative_humidity_2m"
        f"&temperature_unit=celsius" 
        f"&wind_speed_unit=mph"        
        f"&timezone=auto"
    )
    
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()["current"]
        
        temp = data["temperature_2m"]
        feels_like = data["apparent_temperature"]
        humidity = data["relative_humidity_2m"]
        wind = data["wind_speed_10m"]
       
        code = data["weather_code"]
        descriptions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            51: "Light drizzle",
            61: "Rain",
            71: "Snow",
            95: "Thunderstorm"
        }
        description = descriptions.get(code, "Unknown")
        
        print(f"\nWeather in {location_name}, {country}:")
        print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} mph")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    print("Simple Weather App (using Open-Meteo API)")
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        if city.lower() == "quit":
            break
        if city:
            get_weather(city)
        else:
=======
import requests

def get_weather(city):
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en"
    geo_response = requests.get(geocode_url)
    
    if geo_response.status_code != 200 or not geo_response.json().get("results"):
        print("City not found. Please check the spelling and try again.")
        return
    
    lat = geo_response.json()["results"][0]["latitude"]
    lon = geo_response.json()["results"][0]["longitude"]
    location_name = geo_response.json()["results"][0]["name"]
    country = geo_response.json()["results"][0].get("country", "")
    
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,apparent_temperature,weather_code,wind_speed_10m,relative_humidity_2m"
        f"&temperature_unit=celsius" 
        f"&wind_speed_unit=mph"        
        f"&timezone=auto"
    )
    
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()["current"]
        
        temp = data["temperature_2m"]
        feels_like = data["apparent_temperature"]
        humidity = data["relative_humidity_2m"]
        wind = data["wind_speed_10m"]
       
        code = data["weather_code"]
        descriptions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            51: "Light drizzle",
            61: "Rain",
            71: "Snow",
            95: "Thunderstorm"
        }
        description = descriptions.get(code, "Unknown")
        
        print(f"\nWeather in {location_name}, {country}:")
        print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} mph")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    print("Simple Weather App (using Open-Meteo API)")
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        if city.lower() == "quit":
            break
        if city:
            get_weather(city)
        else:
>>>>>>> f1262d6dc94cd034f43d36d32e84765fed673c25
            print("Please enter a valid city name.")