import requests

url = "https://api.thecatapi.com/v1/images/search?api_key=live_DHcdF4TZpDRP5RMHY5VNj86NQkehhW26qXZBTN0SANB2ARCYgWO2b7WeuISDC9Yu"


response = requests.get(url)


if response.status_code == 200:

    data = response.json()
    
   
    for cat in data:
        print("URL da imagem de gato:", cat["url"])
else:
    print(f"Erro ao acessar a API. Status Code: {response.status_code}")
