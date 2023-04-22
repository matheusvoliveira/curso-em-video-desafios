import requests

currency = str(input('Escolha a moeda que quer a cotação(ex: USD, GBP, EUR): ').upper().strip())
value = int(input('Escolha o valor a ser cotado: '))
api_key = # colocar a sua api key
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency}'
# {currency} na url mostra qual moeda ele vai pegar a cotação

response = requests.get(url)
data = response.json()
#reponse.json() mostra todos os atributos de uma biblioteca
real = data['conversion_rates']['BRL']

if response.status_code == 200:
    if real < value:
        print('{}BRL são {:.2f}{}'.format(value, value / real, currency))
    else:
        print('{}BRL são {:.2f}{}'.format(value, value * real, currency))
else:
    print('Falha ao obter a cotação')