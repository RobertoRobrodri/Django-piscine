import sys, requests
from bs4 import BeautifulSoup

def heroes_journey(article)->str:
	wiki_url = 'https://en.wikipedia.org/' + article
	r = requests.get(wiki_url)
	soup = BeautifulSoup(r.content, 'html.parser')
	#print(soup.prettify())

	# Get first fucking heading
	actual_page = soup.find(id="firstHeading").text
	print(actual_page)
	# Get next link
	first_link = soup.find('a', href=True, title='Food')['href']
	print(first_link)

	

if __name__ == '__main__':
	if len(sys.argv) == 2:
		path_to_philo = []
		#path_to_philo.append(heroes_journey(sys.argv[1]))
		heroes_journey("wiki/" + sys.argv[1])