
names=("Espresso","Cappuccino","Robusta")

class CoffeeMachine:
  def __init__(self,brand='Philips'):
    self.brand = brand

  def makeCoffee(self, name, ingredients): 
    if name in names:
      coffeeDrink = _CoffeeDrink(name, ingredients)
      return coffeeDrink
    else:
      return f'This machine can make only {names} types of Coffee'

class _CoffeeDrink:
    def __init__(self,name,ingredients):
      self.name = name
      self.ingredients = ingredients

    def __str__(self):
      return f" --- Your order is: {self.name} and ingridients {self.ingredients}"


