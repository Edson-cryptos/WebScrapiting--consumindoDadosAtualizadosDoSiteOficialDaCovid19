from bs4 import BeautifulSoup
import requests

link = requests.get("https://bitcoin.org").content  # O link recebe a informacao da requisicao http, que esta sendo feita no site https://bitcoin.org
soup = BeautifulSoup(link, 'html.parser')

endereco_doacao_btc = soup.find("a", class_="donation-btc-address")

print(soup.prettify()) # estamos imprimindo o codigo html do site

print(soup.find_all())

print(soup.title.string) # estamos a buscar o titulo do site

print(soup.find('admin')) # estamos procurando o nome do administrador, caso seja possivel acha-lo

print(soup.p.string)

print(endereco_doacao_btc.string)

