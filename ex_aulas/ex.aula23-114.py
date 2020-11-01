import requests
try:
    response = requests.get('http://www.pudim.com.br/')
    print('\033[33mConsegui acessar o site do Pudim com sucesso!\033[m')
except:
    print('\033[31mNão consegui acessar o site do Pudim no momendo :(\033[m')
