import os
from logoforauctionbid import logo
os.system('cls')
print(logo)
t=1
auction={}
while t:
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: "))
    auction[name]=bid
    q=input("want to continue enter yes else no : ")
    if q=="no":
        t=0
    os.system('cls')
m=0
n=''
for i,j in auction.items():
    if j>m:
        m=j
        n=i
print(f"The maximum bidder is {n} with ${m}")