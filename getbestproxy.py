import requests
from colorama import init, Fore
init()

def bestProxy(pais="all"):
    proxies_request = requests.get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country={pais}&ssl=all&anonymity=all")
    proxies_lista = proxies_request.content.decode('utf-8')
    proxies_lista = proxies_lista.replace("\r", "")
    proxies_lista = proxies_lista.split('\n')
    working = 0
    menor_lat = 99999
    working_proxy = 0
    print("\n")
    for proxy in proxies_lista:
        if working < 5:
            print(Fore.RESET + f"Testando Proxy {proxy}")
            try:
                teste_request = requests.get("https://www.google.com.br/", proxies={'http':proxy, 'https': proxy}, timeout=5)
                latencia = float(f"{teste_request.elapsed.total_seconds():.2f}")
                print(Fore.GREEN + f"Tempo de resposta: {latencia} Segundos\n")
                print(Fore.RESET)
                working+=1
                if latencia < menor_lat:
                    menor_lat = latencia
                    working_proxy = proxy
            except:
                print(Fore.RED + f"Proxy {proxy} mal sucedido.\n")
                print(Fore.RESET)
        else:
            break
    print(f"O Proxy {working_proxy} teve a menot latência de {Fore.GREEN + f'{menor_lat}'}.")
    print(Fore.RESET)
    return working_proxy.split(":")