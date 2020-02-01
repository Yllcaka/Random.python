import requests
from bs4 import BeautifulSoup
url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
for link in soup.find_all('p'):
    print(link.get_text())