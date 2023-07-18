import csv
import datetime as dt
import random
import smtplib

email="t72053126@gmail.com"
password="sxihhfqnxzojinkg"
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

day=dt.datetime.now().day
month=dt.datetime.now().month
name={}
with open("birthdays.csv") as file:
    birthday_file=csv.DictReader(file)

    for i in birthday_file:
        
        if day==int(i['day']) and month==int(i['month']):
            name[i['name']]=i['email']
            

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

random_number=random.randint(1,3)

with open(f".\letter_templates\letter_{random_number}.txt") as file:
    data=file.read()

    for i in name.items():
        
        new_data=data.replace("[NAME]",i[0])

        
# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            #tls - transport layer security
            connection.starttls()#this will encrypt the email so other cannot read the message while transfering 
            connection.login(user=email,password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=i[1],
                msg=f"Subject : Birthday wishes \n\n {new_data}")



