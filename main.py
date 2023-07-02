import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response = response.json()
    print(parsed_response)
except:
    print("Ответ не является JSON")