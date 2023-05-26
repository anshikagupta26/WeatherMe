# Weather CLI
A command-line tool that accepts a city's name and returns the current weather forecast.

<img width="500" alt="Screenshot 2023-05-27 at 4 09 05 AM" src="https://github.com/anshikagupta26/WeatherMe/assets/71334544/2ff78c96-79d2-46a4-8741-723f1f5ec7bd">

# Commands

### For MacOS/Linux
```
Usage:
    ./weather.sh --help            # to get help message
    ./weather.sh <city-name>       # to get weather data for a city

Example 
    ./weather.sh Jhansi    
```

### For Windows
```
Usage:
    ./weather.bat --help            # to get help message
    ./weather.bat <city-name>       # to get weather data for a city

Example 
    ./weather.bat Jhansi    
```

# GitHub Copilot Suggestions 
The following demonstrate the suggestions provided by GitHub Copilot.
1.	Error handling: GitHub Copilot suggests using a try-except block to catch potential exceptions when making the API request. This helps to handle possible network errors or issues with the API endpoint.
2.	Error message: In case an exception occurs during the API request, GitHub Copilot suggests printing an informative error message that includes the exception details. This helps in providing useful feedback to the user.
3.	Data parsing: GitHub Copilot provides suggestions for parsing the response JSON data. It suggests using the .get() method to safely access nested dictionary values and provides default values in case the data is missing or not in the expected format.
4.	Printing weather information: GitHub Copilot suggests using conditional statements to print the temperature and weather description only if the data is available. This improves the code's readability and handles cases where certain data fields may be missing from the API response.
