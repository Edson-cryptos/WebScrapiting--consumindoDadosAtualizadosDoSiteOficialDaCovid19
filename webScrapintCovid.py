from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.gavi.org/covid19").content

soup = BeautifulSoup('site, html.parser')

print(soup.prettify())
