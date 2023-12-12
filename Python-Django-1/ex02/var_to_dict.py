def convert_list():
	d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'),
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]
	return_dictionary(d)
	
def return_dictionary(list_to_convert):
	new_dictionary = {}
	for element in list_to_convert:
		(value, key) = element
		new_dictionary.update({key:value})
	for key, value in new_dictionary.items():
		print(key, " : ", value)

if __name__ == '__main__':
	convert_list()