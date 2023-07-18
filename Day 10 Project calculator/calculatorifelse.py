from calculatorlogo import logo
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def operator(operation,a,b):
    if operation=='+':
        output=add(a,b)
    elif operation=='-':
        output=sub(a,b)
    elif operation=='*':
        output=mul(a,b)
    else:
        output=div(a,b)
    return output

def get(a):
    operation=input(" + , - , * , / \n")
    b=int(input("Number 2 : "))
    output=operator(operation,a,b)
    print(f" {a} + {b} = {output}")
    return output
temp=1
print(logo)
while temp:
    output=0
    cal=1
    a=int(input("Number 1 : "))
    operation=input(" + , - , * , / \n")
    b=int(input("Number 2 : "))
    output=operator(operation,a,b)
    print(f" {a} {operation} {b} = {output}")
    temp=int(input("Enter 1 to continue else 0 "))
    if not temp: break
    
    while cal:
        cal=int(input(f"Enter 1 to continue with output {output} else enter 0 for new calculation"))
        if not cal: break
        output=get(output)
        temp=int(input("Enter 1 to continue else 0 "))
        if not temp: break


        
        
        
    


