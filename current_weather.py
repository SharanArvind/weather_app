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


# Example usage:
city_name = "Pondicherry"  # Example city
print(get_current_weather(city_name))
