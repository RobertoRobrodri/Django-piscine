import sys, os, re
import settings

def my_sed(output, template):
	pattern = re.compile("\{([^}]+)\}")
	for line in template:
		matches = re.findall(pattern, line)
		print(matches)
		if len(matches) > 0:
			for match in matches:
				output.write(re.sub(pattern, getattr(settings, match), line))
		else:
			output.write(line)
if __name__ == '__main__':
	template = [file for file in os.listdir('.') if file.endswith('.template')]
	if len(template) != 1:
		raise ValueError('Too many templates') 
	with open("file.html", "w") as output:
		with open(template[0], "r") as read_file:
			my_sed(output, read_file)
