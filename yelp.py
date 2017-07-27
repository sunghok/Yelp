import pandas as pd
import requests
from bs4 import BeautifulSoup
from collections import Counter


def collect_reviews(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "lxml")
	reviews = soup.find_all("p",{"lang": "en"})
	for review in reviews:
		yelp.append(review.text)


def count_words_fast(text):
	text = text.lower()
	skips = [".",",",";",":","'",'"',"the","and","a","is","in"]
	for ch in skips:
		text = text.replace(ch, "")

	word_counts = Counter(text.split(" "))
	return word_counts





yelp = []

yelp = ''.join(yelp)


counted = count_words_fast(yelp)
print(counted)



