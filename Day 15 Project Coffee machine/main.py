MENU = {
     "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients":
        {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

water = 300
milk = 200
coffee = 100
money = 0
condition = 1


def amount():
    print("\nPlease Insert coins \n")
    quarters=int(input("Number of quarters : "))*0.25
    dimes=int(input("Number of dimes : "))*0.1
    nickels=int(input("Number of nickels : "))*0.05
    pennies= int(input("Number of pennies : ")) * 0.01
    return round(quarters+dimes+nickels+pennies, 2)


def report():
    print(f"\nAvailable Resources\n\nWater : {water}\nMilk : {milk}\nCoffee : {coffee}\nMoney : ${money}\n")


def check_espresso():
    if MENU['espresso']['ingredients']['water'] > water:
        print("\nWater is not enough in coffee machine...")
        return False
    elif MENU['espresso']['ingredients']['coffee'] > coffee:
        print("\nCoffee is not enough in coffee machine...")
        return False
    return True


def check_coffee(co):
    if MENU[co]['ingredients']['water'] > water:
        print("\nWater is not enough in coffee machine...")
        return False
    elif MENU[co]['ingredients']['milk'] > milk:
        print("\nMilk is not enough in coffee machine...")
        return False
    elif MENU[co]['ingredients']['coffee'] > coffee:
        print("\nCoffee is not enough in coffee machine...")
        return False
    return True


while condition:
    dish = int(input("\n1.Espresso\n2.Latte\n3.Cappuccino\n4.Report\n5.OFF\nWhat would you like to choose : "))
    if dish == 1:
        if check_espresso():
            cash = amount()
            if MENU['espresso']['cost'] <= cash:
                money += MENU['espresso']['cost']
                print(f"\nHave Your Espresso...\nHave your change ${round(cash-MENU['espresso']['cost'],2)}")
                water -= MENU['espresso']['ingredients']['water']
                coffee -= MENU['espresso']['ingredients']['coffee']
            else:
                print("\nSorry you don't have enough cash to buy espresso...")
    elif dish == 2 or dish == 3:
        if dish == 2:
            c = 'latte'
        else:
            c = 'cappuccino'
        if check_coffee(c):
            cash = amount()
            if MENU[c]['cost'] <= cash:
                money += MENU[c]['cost']
                print(f"\nHave Your {c}...\nHave your change ${cash - MENU[c]['cost']}")
                water -= MENU[c]['ingredients']['water']
                milk -= MENU[c]['ingredients']['milk']
                coffee -= MENU[c]['ingredients']['coffee']
            else:
                print(f"\nSorry you don't have enough cash to buy {c}...")
    elif dish == 4:
        report()
    elif dish == 5:
        condition = 0
