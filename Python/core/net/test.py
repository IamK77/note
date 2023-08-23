import requests
import json

url = "https://postman-echo.com/post"
data = {
    "name": "张三",
    "age": 18
}

response = requests.post(url, data=data)
json_data = json.loads(response.text)
print(json_data["json"])