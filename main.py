import requests
import key

r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key.API_KEY}")
print(r.status_code)
