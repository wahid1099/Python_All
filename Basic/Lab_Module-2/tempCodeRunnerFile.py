""""
problem: 
DOwnload and change wallpaper automatically

"""
import requests
import json
api_url="https://api.nasa.gov/planetary/apod?api_key=7RkWu7DfDbdIWbQF8ByK5EAv8IfbphLwEfUygAmA"

#get the json
response=requests.get(api_url)
content=response.content.decode("UTF-8")
