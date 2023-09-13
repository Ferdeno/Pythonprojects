import smtplib

import lxml
import requests
from bs4 import BeautifulSoup

url="https://www.amazon.com/kwmobile-Silicone-Compatible-Oneplus-Stick/dp/B0B96SV8TY/ref=sr_1_2?keywords=oneplus%2Bnord%2Bbuds%2B2%2Bcase%2Bcover&qid=1693802894&sprefix=oneplus%2Bnord%2Bbuds%2B%2Caps%2C397&sr=8-2&th=1"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language":"en-GB-oxendict,en-US;q=0.9,en;q=0.8,ta;q=0.7",
    "Content-Type":"text"
}

response=requests.get(url,headers=header)

email="t72053126@gmail.com"
password="emtfvnduldqzafdw"

soup=BeautifulSoup(response.content,"html.parser")
price=soup.find(class_="a-offscreen").get_text()
print(price)
price_without_currency = float(price.split("$")[1])
if price_without_currency<9.0:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="ferdenoferdi@gmail.com",
            msg=f"Subject : Deal of the day \n\n The product {url} price is low this is the right time to buy it ")
        print("Mail sent!!!")



