from bs4 import BeautifulSoup
import requests
import re
from typing import Dict, Set

def paragraph_mentions(text: str, keyword: str)-> bool:
       soup = BeautifulSoup(text, 'html5lib')
       p = [p.get_text() for p in soup('p')]
       return any(keyword.lower() in paragraph.lower() for paragraph in p)

url = ("https://www.house.gov/representatives")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')

all_urls = [a['href'] for a in soup ('a') if a.has_attr('href')]

print(len(all_urls))
for url in all_urls:
    print(url, "\n")


regex = r'^https?://.*\.house\.gov/?$'

assert re.match(regex, "http://joel.house.gov")
assert re.match(regex, "https://joel.house.gov/")
assert not re.match(regex, "http://joel.house.gov.com")
assert not re.match(regex, "https://joel.house.gov/biography")

good_urls = [url for url in all_urls if re.match(regex,url)]
good_urls = list(set(good_urls))
print(len(good_urls))

press_realeases: Dict[str, Set[str]] = {}
for house_url in good_urls:
       html = requests.get(house_url).text
       soup = BeautifulSoup(html, 'html5lib')
       pr_links = [a['href'] for a in soup('a') if 'press release' in a.text.lower()]
       print(f"{house_url}:{pr_links}")
       press_realeases[house_url] = pr_links
       
for house_url, pr_links in press_realeases.items():
       for pr_link in pr_links:
              html = requests.get(pr_link).text
              if paragraph_mentions(html, "healthcare"):
                     print(f"{house_url} has a press release about healthcare: {pr_link}")
       
       
       
