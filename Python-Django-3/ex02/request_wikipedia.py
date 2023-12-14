import sys, json, requests, dewiki

def get_wiki_article(subject):
	wiki_url = 'https://en.wikipedia.org/w/api.php'
	params = {
        'action': 'query',
        'format': 'json',
        'titles': subject,
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
    }

	r = requests.get(wiki_url, params)
	article = r.json()
	page = next(iter(article['query']['pages'].values()))
	print(page['extract'])

if __name__ == '__main__':
	if len(sys.argv) == 2:
		get_wiki_article(sys.argv[1])