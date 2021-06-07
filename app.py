# Main Module Consumer

from coffee import *

p = CoffeeMachine()
ingredient0 = {"Water": "100 ml", "Cofee": "10 gr", "Sugar": "2 gr"}
ingredient1 = {"Water": "200 ml", "Milk": "100 ml", "Cofee": "15 gr", "Sugar": "2 gr"}
ingredient2 = {"Water": "70 ml", "Cofee": "10 gr", "Sugar": "2 gr"}


espresso = p.makeCoffee(names[0], ingredient0)
cappuccino = p.makeCoffee(names[1], ingredient1)
robusta = p.makeCoffee(names[2], ingredient2)

print(espresso)
print(cappuccino)
print(robusta)

