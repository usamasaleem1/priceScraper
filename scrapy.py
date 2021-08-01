import requests
from bs4 import BeautifulSoup

URL = 'https://www.newegg.ca/amd-ryzen-7-5800x/p/N82E16819113665?Item=N82E16819113665&cm_sp=Homepage_dailydeals-_-P0_19-113-665-_-07312021'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# price = soup.find(class_='price-current')
price = soup.find_all('li', class_='price-current')
output = []


for soup in price:
    output.append(soup.find("strong").get_text())
    output.append(soup.find("sup").get_text())
price=float((output[0]+output[1]))

print(price)
print(type(price))