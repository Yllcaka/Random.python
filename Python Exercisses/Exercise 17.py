import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Web_scraping"
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
title = soup.find('span', 'articletitle')
for story_heading in soup.find_all(class_ ="toctext" ):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())