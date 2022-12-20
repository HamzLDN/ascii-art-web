import requests

url = "http://51.195.187.145/ascii-art"

data = {
    "ascii-data": "Hello World!",
    "fonts": "standard"
}

with requests.session() as s:
    r = s.post(url, data=data)
    print(r.text.replace("&#39;", "'"))