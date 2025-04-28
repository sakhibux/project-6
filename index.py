






# Base class
class Beverage:
    def get_description(self):
        return "Unknown Beverage"
    
    def cost(self):
        return 0

# Concrete class
class Coffee(Beverage):
    def get_description(self):
        return "Simple Coffee"
    
    def cost(self):
        return 5

# Decorator Base Class
class BeverageDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage

# Concrete Decorators
class MilkDecorator(BeverageDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Milk"
    
    def cost(self):
        return self.beverage.cost() + 1.5

class SugarDecorator(BeverageDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Sugar"
    
    def cost(self):
        return self.beverage.cost() + 0.5

# --- Using the classes ---

# Step 1: Simple Coffee
simple_coffee = Coffee()
print(f"Order 1: {simple_coffee.get_description()} | Cost: ${simple_coffee.cost()}")

# Step 2: Coffee + Milk
coffee_with_milk = MilkDecorator(simple_coffee)
print(f"Order 2: {coffee_with_milk.get_description()} | Cost: ${coffee_with_milk.cost()}")

# Step 3: Coffee + Milk + Sugar
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(f"Order 3: {coffee_with_milk_and_sugar.get_description()} | Cost: ${coffee_with_milk_and_sugar.cost()}")