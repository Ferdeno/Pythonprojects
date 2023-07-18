# import smtplib

# email="t72053126@gmail.com"
# password="sxihhfqnxzojinkg"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     #tls - transport layer security
#     connection.starttls()#this will encrypt the email so other cannot read the message while transfering 
#     connection.login(user=email,password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs="ferdenoferdi@gmail.com",
#         msg="Subject : Heading \n\n This is the body")
#     # with open("quotes.txt","r") as file:
#     #     connection.sendmail(from_addr=email,to_addrs="ferdenoferdi@gmail.com",msg=file.read())
# connection.close()

import datetime as dt

now=dt.datetime.now()
print(type(now))

year=now.year
weekday=now.weekday()
print(weekday)

month=now.month
print(month)

data_of_birth=dt.datetime(year=2002,month=12,day=10)
print(data_of_birth)

data_of_birth_hour=dt.datetime(year=2002,month=12,day=10,hour=15,minute=30)
print(data_of_birth_hour)