import requests
import time
import json


deg_sym = '°'

#Getting cityName from user
def city():
    cityName = input("Enter City Name: ")

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={YOUR API KEY}&units=metric'.format(cityName)

    #Making request
    response = requests.get(url)
    data = response.json()
    printData(data)

#Getting user's current location
def currentLocation():
    ipResponse = requests.get('https://ipinfo.io/')
    data = ipResponse.json()
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]

    cityName = data['city']

    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={YOUR API KEY}&units=metric'.format(latitude, longitude)
    response = requests.get(url)
    data = response.json()

    time.sleep(1)
    
    print("Your are currently in: {}".format(cityName))
    printData(data)


def printData(data):
    # cityName = data['city']
    temp = data['main']['temp'] #Temperature
    humidity = data['main']['humidity'] #Humidity
    windDegree = data['wind']['deg'] #Wind degree
    windSpeed = data['wind']['speed'] #Wind speed
    description = data['weather'][0]['description'] #Current forecast

    time.sleep(0.5)
    print("Getting weather information...")
    time.sleep(0.5)
    print("Temperature: {}{}C".format(temp,deg_sym))
    time.sleep(0.5)
    print("Humidity: {}".format(humidity))
    time.sleep(0.5)
    print("Wind Degree: {}m/s".format(windDegree))
    time.sleep(0.5)
    print("Wind Speed: {}".format(windSpeed)) 
    time.sleep(0.5)
    print("Forecast: {}".format(description))
    time.sleep(1.5)


def menu():
    print("==== Weather Forecast ====")
    print("1. Current location")
    print("2. Enter City Name")
    print("3. Exit")


def main():
    menu()
    choices = input("Choose one of the option above to proceed: ")

    if choices == '1':
        currentLocation()
        main()
    elif choices == '2':
        city()
        main()
    elif choices == '3':
        exit
        time.sleep(1)
        print("==== Have A Nice Day ==== ")
    else:
        main()
        

if __name__ == '__main__':
    main()
