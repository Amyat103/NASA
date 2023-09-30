import requests
import key
import json
from PIL import Image
from io import BytesIO

r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key.API_KEY}")
print(r.status_code)

response = json.loads(r.content)
print(response)

pic_request = requests.get(response["hdurl"])
pic_conv = Image.open(BytesIO(pic_request.content))
pic_conv.show()
