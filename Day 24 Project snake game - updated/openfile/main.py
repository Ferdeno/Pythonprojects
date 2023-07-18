# normal method of opening and closing file manually
file=open("deno.txt")
content=file.read()
print(content)
file.close()

# using with the file will get open and will close automatically when the control goes out of the block of code
# mode r = read w = write a = append
# when the file is not there it will create only works in mode = w
with open("deno.txt",mode="a") as file:
    # content=file.read()
    # print(content)
    file.write("vannakam")
    # print(content)
