from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
coffermaker=CoffeeMaker()
moneymachine=MoneyMachine()
condition = 1
while condition:
    dish = int(input("\n1.Espresso\n2.Latte\n3.Cappuccino\n4.Report\n5.OFF\nWhat would you like to choose : "))
    if dish == 4:
        print("\n")
        coffermaker.report()
        moneymachine.report()
    elif dish == 5:
        condition = 0
    else:
        if dish == 1:
            dish = "espresso"
        elif dish == 2:
            dish = "latte"
        elif dish == 3:
            dish = "cappuccino"
        else :
            dish == ""

        if menu.find_drink(dish) != None:
            dish = menu.find_drink(dish)
            if coffermaker.is_resource_sufficient(dish) and moneymachine.make_payment(dish.cost):
                coffermaker.make_coffee(dish)
