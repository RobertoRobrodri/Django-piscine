import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
	broken_count = 10

	def __init__(self) -> None:
		broken_count = 10

	def repair(self):
		self.broken_count = 10
	
	def serve(self, drink:HotBeverage) -> HotBeverage():
		try:
			if self.broken_count > 0:
				self.broken_count - 1
				if random.randint(0, 5) == 0:
					return CoffeeMachine.EmptyCup()
				return drink
			else:
				raise self.BrokenMachineException
		except self.BrokenMachineException:
			print(self.BrokenMachineException)


	class EmptyCup(HotBeverage):
		def __init__(self):
			super().__init__(0.90, "empty cup")

		def description(self)->str:
			return "An empty cup?! Gimme my money back!"
		
	class BrokenMachineException(Exception):
		def __init__(self) -> None:
			super().__init__("This coffee machine has to be repaired.")

if __name__ == '__main__':
	agua = HotBeverage()
	cafe = Coffee()
	te   = Tea()
	choco= Chocolate()
	capu = Cappuccino()
	print(agua.__str__())
	print(cafe.__str__())
	print(te.__str__())
	print(choco.__str__())
	print(capu.__str__())


	cameracafe = CoffeeMachine()
	new_choco = cameracafe.serve(choco)
	print(new_choco.__str__())