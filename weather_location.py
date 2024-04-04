import urllib.request
from bs4 import BeautifulSoup

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

city_name = input("Enter city name: ")
print(get_weather_forecast(city_name))
