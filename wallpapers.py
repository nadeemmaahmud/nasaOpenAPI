import requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

#getting the json
request = requests.get(api_url)
content = request.content.decode('UTF-8')

#converting string to json
dict_content = json.loads(content)

#getting the image url
url = dict_content['url']

#downloading the image
response1 = requests.get(url)

#downloading the image
with open("Nasa.png", "wb") as image:
    image.write(response1.content)

#PyWallpaper.change_wallpaper("/Users/nadimmahmud/Documents/Coding/Phitron/Nasa.png")