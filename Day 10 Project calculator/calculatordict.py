from calculatorlogo import logo
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def findoperator():
    for i in operation:
        print(i,end=" ")
    return input("\nEnter the operation : ")

def get(a):
    operator=findoperator()
    b=int(input("Number 2 : "))
    output=operation[operator](a,b)
    print(f" {a} + {b} = {output}")
    return output
temp=1
print(logo)
operation={"+":add,"-":sub,"*":mul,"/":div}
while temp:
    output=0
    cal=1
    a=int(input("Number 1 : "))
    operator=findoperator()
    b=int(input("\nNumber 2 : "))
    output=operation[operator](a,b)
    print(f" {a} {operator} {b} = {output}")
    temp=int(input("Enter 1 to continue else 0 "))
    if not temp: break
    
    while cal:
        cal=int(input(f"Enter 1 to continue with output {output} else enter 0 for new calculation"))
        if not cal: break
        output=get(output)
        temp=int(input("Enter 1 to continue else 0 "))
        if not temp: break


        
        
        
    


