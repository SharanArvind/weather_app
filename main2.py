import urllib.request
from bs4 import BeautifulSoup

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

# Example usage:
city_name = input("Enter city name: ")
city_weather_forecast = get_city_weather_forecast(city_name)
for period, forecast in city_weather_forecast.items():
    print(f"{period}: {forecast}")
