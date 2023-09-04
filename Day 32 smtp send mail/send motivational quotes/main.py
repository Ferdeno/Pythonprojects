import datetime as dt
import random
import smtplib

weekday=dt.datetime.now().weekday()
print(weekday)
email="t72053126@gmail.com"
password="emtfvnduldqzafdw"

if weekday==0:
    with open("quotes.txt") as file:
        quotes=file.readlines()
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    #tls - transport layer security
        connection.starttls()#this will encrypt the email so other cannot read the message while transfering 
        connection.login(user=email,password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="ferdenoferdi@gmail.com",
            msg=f"Subject : Quotes of the day \n\n {random.choice(quotes)}")
print(random.choice(quotes))
