import requests
import key
import json
from PIL import Image
from io import BytesIO

#Astronomy Picture of the Day (APOD)

date_param = {
    "date": "2022-10-30"
}

count_param = {
    "count": 3
}

choice = input("params")

if choice == "date":
    r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key.API_KEY}", params=date_param)
    print(r.status_code)
    response = json.loads(r.content)
    pic_request = requests.get(response["hdurl"])
    pic_conv = Image.open(BytesIO(pic_request.content))
    pic_conv.show()
elif choice == "count":
    r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key.API_KEY}", params=count_param)
    print(r.status_code)
    response = json.loads(r.content)
