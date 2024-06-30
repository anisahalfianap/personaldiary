import requests

api_key = '17472b83-601e-4efc-9fb4-73a90f96a701'
word = 'monkey'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)