import requests

#@yasinkuyu 08/09/2017

def check_internet():
    url = "http://pudim.com.br"
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
    except requests.ConnectionError:
        print(f'\033[31;3mO site pudin está fora do ar!\033[m')
    else:
        print(f'\033[32;3mO site pudin está online!\033[m')

result = check_internet()

