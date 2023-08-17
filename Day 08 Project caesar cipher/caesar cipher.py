
def caesar(text,shift,condition):
    for i in text:
        if i in alphabet and condition=="encode":
            print(alphabet[(alphabet.index(i)+shift)%26],end="")
        elif i in alphabet and condition=="decode":
            print(alphabet[(alphabet.index(i)-shift)%26],end="")
        else:
            print(i,end="")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
temp=1
while temp:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    n=int(input("\n1 or 0"))
    if not n:
        temp=0
