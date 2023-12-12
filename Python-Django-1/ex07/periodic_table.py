import sys

def write_html(element, html_page):
	html_page.write("\t\t<h4>" + element["name"] + "</h4>\n")
	html_page.write("\t\t\t<ul>\n")
	html_page.write("\t\t\t\t<li>" + element["position"] + "</li>\n")
	html_page.write("\t\t\t\t<li>" + element["number"] + "</li>\n")
	html_page.write("\t\t\t\t<li>" + element["small"] + "</li>\n")
	html_page.write("\t\t\t\t<li>" + element["molar"] + "</li>\n")
	html_page.write("\t\t\t\t<li>" + element["electron"] + "</li>\n")
	html_page.write("\t\t\t</ul>\n")
		

if __name__ == '__main__':
	with open("periodic_table.txt", "r") as element:
		with open("output.html", "w") as html_page:
			html_page.write("<body>\n")
			html_page.write("\t<table>\n \t\t<tr>\n")
			html_page.write("\t\t<td style=\"border: 1px solid black; padding:10px\">")
			for line in element:
				el = line.split("=")
				result = dict((value.strip().split(":") for value in el[1].split(", ")))
				result["name"] = el[0].strip()
				write_html(result, html_page)
			html_page.write("\t\t</tr>\n \t</table>\n")
			html_page.write("</body>\n")
		