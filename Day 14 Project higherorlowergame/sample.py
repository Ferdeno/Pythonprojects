from higherorlowergamedatatxt import data
import os
import random
os.system('cls')
dic=random.choice(data)
print(f"Name : {dic['name']} \nDescription : {dic['description']}\nCountry : {dic['country']}")