# # try:
# #     file=open("data.txt","r")
# # except:
# #     print("Error")


# try:
#     file=open("data.txt","r")
#     # file.write("Ferdeno")
#     dictionary={"fer":"deno"}
#     print(dictionary["fer"])

# except FileNotFoundError:
#     print("Error , creating a new file")
    

# except KeyError as e:
#     print(f"{e} Key doesn't exist")

# #if try runs successfully then else will execute
# else:
#     content=file.read()
#     print(content)

# #finally will execute always after completing all the above one
# # ie anything happens the finally will execute
# finally:
#     file.close()
#     raise KeyError #raise will throw an error 
#     raise TypeError("HII")#raise will throw an error with a message


height=int(input("Height : "))
weight=int(input("Weight : "))

if height>4:
    raise ValueError("height should be less than 4")

print("BMI : ",weight/height**2)

except 