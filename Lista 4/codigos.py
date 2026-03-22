from bs4 import BeautifulSoup
import requests

url = ("https://raw.githubusercontent.com/"
       "joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')
print(soup)
print("------------------------")
print(html)

important_paragraphs = soup('p', {'class': 'important'})

spans_inside_divs = [span 
                     for div in soup('div') 
                     for span in div('span')]

print(important_paragraphs)
print("------------------------")
print(spans_inside_divs)


congresso = "https://www.house.gov/representatives"