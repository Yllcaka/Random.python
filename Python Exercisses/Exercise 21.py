import requests
from bs4 import BeautifulSoup
url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
def Printi():
    a = ''
    for link in soup.find_all('p') [:-5]:
        b = (link.get_text())
        a = a + b + '\n' + '\n'
    return a
with open('UltraFunTime Exercise 21.txt', 'w') as open_file:
    open_file.write(Printi())