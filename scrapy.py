import requests
import smtplib
from bs4 import BeautifulSoup
URL = input("Hey, enter a newegg URL you would like to set an alert for, then press Enter: ")

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

# Method to send email when price criteria is met
def notify():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('saleemusama1@gmail.com', 'onetimepassword here')
    subject = '[NEWEGG] Price Alert!'
    body = 'Hey! The price has gone down. Its now ' + str(price) + ', heres the product link: ' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('saleemusama1@gmail.com', recipient, msg)
    print('PRICE IS LOWER! Email sent!')
    server.quit()

# Scraping data from site URL 
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
price = soup.find_all('li', class_='price-current')
output = []

for soup in price:
    output.append(soup.find("strong").get_text())
    output.append(soup.find("sup").get_text())
price=((output[0]+output[1]))
price = float(price.replace(',', ''))
print(price)

priceToCheck = input("\nIt seems the current price is " + str(price) + ", what would you like the price to be? Ex: 420.69: ")
priceToCheck = float(priceToCheck)
price = float(price)
recipient = input("\nEnter the email you want the alert to be sent to: ")

# Criteria to send email
if(price > priceToCheck):
    notify()
else: 
    print("Gotcha. It's currently above what you want to purchase it for, so i'll notify you when its at " + str(priceToCheck) + " or lower! :)")
    

