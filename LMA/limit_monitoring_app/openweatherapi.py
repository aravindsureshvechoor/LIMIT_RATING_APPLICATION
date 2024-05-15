from django.core.management.base import BaseCommand
import requests
import time
from .models import Criterias

class Command(BaseCommand):
    help = 'Update weather data from OpenWeatherMap every 5 minutes'

    def handle(self, *args, **kwargs):
        while True:
            api_url = 'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=657298c1329ea0d2ed4b179d4e187b53'

            response = requests.get(api_url)
            if response.ok:
                data = response.json()
                # Convert Kelvin temperature from API response to Fahrenheit
                current_temperature_kelvin = data['current']['temp']
                current_temperature_celsius = (current_temperature_kelvin - 273.15)

                # Iterate over all Criterias instances
                for criteria in Criterias.objects.all():
                    # Compare Fahrenheit temperature with the Temperature field of each instance
                    if criteria.comparison_operator == '<' and current_temperature_celsius < criteria.Temperature:
                        criteria.status = True
                    elif criteria.comparison_operator == '>' and current_temperature_celsius > criteria.Temperature:
                        criteria.status = True
                    elif criteria.comparison_operator == '==' and current_temperature_celsius == criteria.Temperature:
                        criteria.status = True

                    criteria.save()
                
                print("Weather data updated successfully.")
            else:
                print('Error:', response.status_code)

            # Sleep for 5 minutes
            time.sleep(5 * 60)
