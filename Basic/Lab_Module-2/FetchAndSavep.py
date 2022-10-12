""""
problem: 
DOwnload and change wallpaper automatically

"""

# library modules
import requests
import json
import PyWallpaper

import os

# api key wth url
api_url="https://api.nasa.gov/planetary/apod?api_key=7RkWu7DfDbdIWbQF8ByK5EAv8IfbphLwEfUygAmA"

#get the json
response=requests.get(api_url)
content=response.content.decode("UTF-8")

# print(content)

# conver string to json

dict_content=json.loads(content)

# print(type(dict_content))

# get image url
image_url=dict_content['hdurl']

# print(image_url)


# download the image 

res=requests.get(image_url)
# print(res)

#save the image to pc


with open('apond.png','wb') as image:
    image.write(res.content)


#set as wallpaper of my screeen

# PyWallpaper.change_wallpaper('/media/wahid/CEFE29E2FE29C3951/Python_programming hero/apond.png')


url = "file://" + os.getcwd() + "/apond.png"
# fullurl = "file:///home/ruhulaminjr/Desktop/Phitron/Python/nas-wallpaper/wallpic.png"
# print(url)
os.system(f'gsettings set org.gnome.desktop.background picture-uri-dark {url}')
# gsettings set org.gnome.desktop.background picture-uri "file://path_to_file"