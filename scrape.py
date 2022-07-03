from bs4 import BeautifulSoup
import requests

url = "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)
print(page)

soup = BeautifulSoup(page.content, 'html.parser')
