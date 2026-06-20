#Modules and Real API Calls
#Built in Modules


# import random
# import math
# import datetime

# # random
# print(random.randint(1, 100))

# # math
# print(math.sqrt(16))
# print(math.pi)

# # datetime
# today = datetime.datetime.now()
# print(today)


# import requests

# api_key = "59761a3f0c36256a58da95cc5585b9ef"

# city = input("Enter city name: ")

# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# response = requests.get(url)
# data = response.json()

# if data["cod"] == 200:
#     temp = data["main"]["temp"]
#     humidity = data["main"]["humidity"]
#     description = data["weather"][0]["description"]
    
#     print(f"\nWeather in {city}:")
#     print(f"Temperature: {temp}°C")
#     print(f"Humidity: {humidity}%")
#     print(f"Condition: {description}")
# else:
#     print("City not found!")




# Weather App

import requests

api_key = "59761a3f0c36256a58da95cc5585b9ef"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        feels_like = data["main"]["feels_like"]

        print(f"\nWeather in {city}:")
        print(f"Temperature : {temp}°C")
        print(f"Feels like  : {feels_like}°C")
        print(f"Humidity    : {humidity}%")
        print(f"Condition   : {description}")
    else:
        print("City not found!")

except:
    print("No internet connection!")