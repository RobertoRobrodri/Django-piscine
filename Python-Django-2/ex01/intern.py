class intern:
	name = "My name? I’m nobody, an intern, I have no name."
	
	def __init__(self, str=None):
		if str != None:
			self.name = str

	def __str__(self)->str:
		return self.name

	class coffee:

		def __str__(self)->str:
			return "This is the worst coffee you ever tasted."

	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")
   
	def make_coffee(self)->coffee:
		return intern.coffee()
	
if __name__ == '__main__':
	interno = intern()
	print(interno.__str__())
	print(interno.make_coffee())
