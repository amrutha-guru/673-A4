#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Q1 Weather program

import requests

#Using API key from the OpenWeatherMap API Website
API_KEY = "e6c7ddc5b07bd19ea56b29df9c485f45"

def get_weather(location):
  #Passes location entered by user as argument and returns weather information on that location
  url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
  #Fetches data from OpenWeatherMap API 
  response = requests.get(url)
  #Status = 200 means success and weather info is returned, if not error message is displayed
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: {response.status_code}")
    return None

def main():
  #User prompted to enter city name 
  location = input("Enter city name: ")
  weather_data = get_weather(location)
  #Showing temperature information in Celcius and description as a few words
  if weather_data:
    temperature = weather_data["main"]["temp"] - 273.15
    feels_like = weather_data["main"]["feels_like"] - 273.15
    description = weather_data["weather"][0]["description"]
    #Printing the results that were extracted above
    print(f"Location: {location}")
    print(f"Temperature: {temperature:.2f}°C")
    print(f"Feels like: {feels_like:.2f}°C")
    print(f"Description: {description}")
  else:
    print("Error retrieving weather data.")

if __name__ == "__main__":
  main()

