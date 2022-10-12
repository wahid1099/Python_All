
import requests
# from PyWallpaper import change_wallpaper
import os


api_url="https://api.nasa.gov/planetary/apod?api_key=7RkWu7DfDbdIWbQF8ByK5EAv8IfbphLwEfUygAmA"

response = requests.get(api_url)
resjson = response.json()
# print(type(resjson))
imgUrl = resjson['url']
imgdata = requests.get(imgUrl)
# print(imgdata.content)

with open('wallpic.png', 'wb') as image:
  image.write(imgdata.content)
url = "file://" + os.getcwd() + "/wallpic.png"
# fullurl = "file:///home/ruhulaminjr/Desktop/Phitron/Python/nas-wallpaper/wallpic.png"
# print(url)
os.system(f'gsettings set org.gnome.desktop.background picture-uri-dark {url}')
# gsettings set org.gnome.desktop.background picture-uri "file://path_to_file"