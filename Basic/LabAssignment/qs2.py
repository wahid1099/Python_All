
import requests
import time

def weather_data():
    api_key="5719806ed25c7e3d959634e8b6707781"
    city_name="Dhaka"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
   
    response = requests.get(url).json()
    temp_kelvin=response['main']['temp']
    celcius=temp_kelvin-273.15
    format_celcius="{:.2f}".format(celcius)
    return format_celcius
   
    


   
while True:
    
    tempretur= weather_data()
    print(f"Tempreture of Dhaka is {tempretur}°C")
    time.sleep(30*60)








  



