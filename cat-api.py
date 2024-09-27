import requests

# URL da API com a chave fornecida
url = "https://api.thecatapi.com/v1/images/search?api_key=live_DHcdF4TZpDRP5RMHY5VNj86NQkehhW26qXZBTN0SANB2ARCYgWO2b7WeuISDC9Yu"

# Fazer uma requisição GET para a URL
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # Converter a resposta em formato JSON
    data = response.json()
    
    # Extrair a URL da imagem e exibir
    for cat in data:
        print("URL da imagem de gato:", cat["url"])
else:
    print(f"Erro ao acessar a API. Status Code: {response.status_code}")
