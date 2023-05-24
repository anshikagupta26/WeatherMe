import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

    # response = requests.get(url)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        #  In case an exception occurs during the API request, 
        # GitHub Copilot suggests printing an informative error 
        # message that includes the exception details. 
        # This helps in providing useful feedback to the user.
        print(f"Failed to fetch weather data: {e}")
        return

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")


def main():
    city_name = input("Enter city name: ")
    get_weather(city_name)

if __name__ == "__main__":
    main()
