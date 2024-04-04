import urllib.request
from bs4 import BeautifulSoup

def get_current_weather(city):
    url = f'https://www.weather-forecast.com/locations/{city}/forecasts/latest'
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        soup = BeautifulSoup(data, 'html.parser')
        current_weather = soup.find(class_='b-forecast__table-description-content').text.strip()
        return f"The current weather in {city} is: {current_weather}"
    except:
        return "Error fetching data"

def get_city_weather_forecast(city):
    url = f'https://www.weather-forecast.com/locations/{city}/forecasts/latest'
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        soup = BeautifulSoup(data, 'html.parser')
        
        # Extracting weather forecast for 1-3 days
        today_forecast = soup.find_all(class_='b-forecast__table-description-content')[0].text.strip()

        # Extracting weather forecast for 4-7 days
        four_to_seven_days_forecast = soup.find_all(class_='b-forecast__table-description-content')[1].text.strip()

        # Extracting 10-day weather forecast
        ten_day_forecast = soup.find_all(class_='b-forecast__table-description-content')[2].text.strip()

        # Extracting weather forecast for next week (10-12 days)
        next_week_forecast = soup.find_all(class_='b-forecast__table-description-content')[3].text.strip()

        return {
            f"{city} Weather Today (1–3 days)": today_forecast,
            f"{city} Weather (4–7 days)": four_to_seven_days_forecast,
            f"10 Day {city} Weather (7–10 days)": ten_day_forecast,
            f"{city} Weather Next Week (10–12 days)": next_week_forecast
        }
    except:
        return "Error fetching data"

def get_weather_forecast(city):
    try:
        url = f'https://www.timeanddate.com/weather/india/{city}'
        response = urllib.request.urlopen(url)
        data = response.read()
        soup = BeautifulSoup(data, 'html.parser')
        weather_info = soup.find('div', class_='h2').text.strip()
        return f"The weather in {city} is {weather_info}"
    except:
        return "Error fetching data"

def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        print("\n1. Get Current Weather")
        print("2. Get Weather Forecast")
        print("3. Get Weather for a Specific Location")
        print("4. Convert Temperature Units")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            city_name = input("Enter city name: ")
            print(get_current_weather(city_name))
        elif choice == '2':
            city_name = input("Enter city name: ")
            city_weather_forecast = get_city_weather_forecast(city_name)
            for period, forecast in city_weather_forecast.items():
                print(f"{period}: {forecast}")
        elif choice == '3':
            city_name = input("Enter city name: ")
            print(get_weather_forecast(city_name))
        elif choice == '4':
            temperature_choice = input("Enter '1' to convert Celsius to Fahrenheit, or '2' to convert Fahrenheit to Celsius: ")
            if temperature_choice == '1':
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
            elif temperature_choice == '2':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius")
            else:
                print("Invalid choice")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice")

        continue_choice = input("Do you want to continue? (yes/no): ")
        if continue_choice.lower() != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
