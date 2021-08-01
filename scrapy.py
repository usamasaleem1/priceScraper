import requests
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.newegg.ca/p/1A0-0077-001A9?Item=9SIAP44EZZ1057'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}


def notify():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('saleemusama1@gmail.com', 'jixhgovxcpfzdjbf')
    subject = '[NEWEGG] Price Alert!'
    body = 'Product Link: ' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('saleemusama1@gmail.com', 'usama.saleem@hotmail.com', msg)
    print('Email sent')
    server.quit()


page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find_all('li', class_='price-current')
output = []

for soup in price:
    output.append(soup.find("strong").get_text())
    output.append(soup.find("sup").get_text())
price=float((output[0]+output[1]))
print(price)

if(price < 100):
    notify()
