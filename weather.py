import requests
import sys

API_KEY = "API_KEY"
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'  # Reset to default color

# GitHub Copilot suggests using a function to fetch weather data from the API.
# This helps in keeping the code modular and easy to understand.
# It also helps in reducing the complexity of the main function.
# The function takes the city name as an argument and returns the weather data.
def get_weather(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

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

    #parse the response and print the weather data is the response is successful
    weather_data = response.json()
    print(GREEN + f"Current weather in {weather_data['name']}:" + RESET)
    print(GREEN + weather_data["weather"][0]["main"] + RESET)
    print(GREEN + weather_data["weather"][0]["description"] + RESET)
    print(GREEN + f"Temperature: {weather_data['main']['temp'] - 273.15:.2f}°C" + RESET)
    print(GREEN + f"Humidity: {weather_data['main']['humidity']}%" + RESET)
    print(GREEN + f"Pressure: {weather_data['main']['pressure']} hPa" + RESET)
    print(GREEN + f"Wind: {weather_data['wind']['speed']} m/s" + RESET) 


# define a function to print the help message
def help():
    print(YELLOW + '''Usage :-
$ ./weather.bat <city_name>         # to get weather data for a city
$ ./weather.bat --help              # to get help message

Example: ./weather.bat jhansi
''' + RESET)

def main():
    # city_name = input("Enter city name: ")
    # get_weather(city_name)

    # GitHub Copilot suggests using the command line arguments to get the city name.
    # This helps in making the program more flexible and easy to use.
    # The user can now pass the city name as a command line argument.
    # This also helps in reducing the complexity of the main function.
    if len(sys.argv) < 2:
        help()
        return
    
    argument1 = sys.argv[1]

    if argument1 == "--help":
        help()
        return
    
    else:
        get_weather(argument1)
    


if __name__ == "__main__":
    main()
