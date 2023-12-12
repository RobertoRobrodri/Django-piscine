class HotBeverage:
	price = 0.30
	name  = "Hot Beverage"

	def __init__(self, price=0.30, name="Hot Beverage")-> None:
		self.price = price
		self.name  = name
	
	def description(self)->str:
		return "Just some hot water in a cup."
	
	def __str__(self)->str:
		placeholder = ("name : {name}\n"
						"price : {price}\n"
						"description : {description}")
		return placeholder.format(name=self.name, price=self.price, description=self.description())

class Coffee(HotBeverage):
	def __init__(self):
		super().__init__(0.40, "coffee")
	def description(self)->str:
		return "A coffee, to stay awake."
	
class Tea(HotBeverage):
	def __init__(self):
		super().__init__(0.30, "tea")

class Chocolate(HotBeverage):
	def __init__(self):
		super().__init__(0.50, "chocolate")
	def description(self)->str:
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
	def __init__(self):
		super().__init__(0.45, "capuccino")
	def description(self)->str:
		return "Un po’ di Italia nella sua tazza!"