# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
t="true"
l="love"
tcount=0
lcount=0
name=name1+name2
name=name.lower()
for i in t:
    tcount+=name.count(i)
for i in l:
    lcount+=name.count(i)
tcount=str(tcount)
lcount=str(lcount)
c=tcount+lcount
c=int(c)
if c<10 or c>90:
    print(f"Your score is {c}, you go together like coke and mentos.")
elif c>40 and c<50:
    print(f"Your score is {c}, you are alright together.")
else:
    print(f"Your score is {c}.")