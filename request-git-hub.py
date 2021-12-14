
# Request titulos github grátis
# este algoritmo busca uma frase de efeito aleatorio de uma API gratis da web


import requests
import json


def get_simples(url):
    response = requests.get(url)
    return response

url_get = 'https://github.com/explore'

response = get_simples(url_get)

print(response.text)