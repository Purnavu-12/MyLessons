import requests

API_KEY = "Weather API_KEY from openweathermap.org"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp}°F (feels like {feels_like}°F)")
        print(f"Condition: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} mph")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)