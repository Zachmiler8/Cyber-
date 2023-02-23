#
# Program :Weather_Final.py
# Author  :Zach Miller
# Date    :February 12, 2023
# Purpose :This program takes a location (city or zip code) and presents 
# the weather information for that location in a readable format. 
#

# imports 
import json, requests


# main function takes input and calls data function.
def main():
  city = 'start'

  # loop until user ends program
  while city != '.':  
    try:
      city = input('Please input your city or zip code or . to end: ')
      if city == '.':
        break
      weather_data(city)
    

    except:
      print('Connection unsuccessful, make sure to enter a valid city or zip code')
      print( )
      main()
    
def weather_data(city):
  print('Connection successful!')
  base_url = 'https://api.openweathermap.org/data/2.5/weather'
  appid = '561cae8dc5d82b66ed89ab97ed7bfebf'

  url = f'{base_url}?q={city}&units=imperial&APPID={appid}'
  print(url)
  print ()

  response = requests.get(url)
  unformatted_data = response.json()

  print(unformatted_data)
  # displays a message with the city name in it that was input
  name = unformatted_data['name']
  print(f'The weather forecast for today in {name} is: ')

  # prints the temperature
  temp = unformatted_data['main']['temp']
  print(f'The current temp is: {temp}')

  # prints the max temperature for the day
  temp_max = unformatted_data['main']['temp_max']
  print(f'The max temp is: {temp_max}')

  # prints the wind speed 
  wind = unformatted_data['wind']['speed']
  print(f'The wind speed is {wind} mph')
  



main()



