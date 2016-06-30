# An app that tells you the geographic coordinates of a place using geopy module in Django

from blessed import Terminal
from geopy import geocoders

term = Terminal()

def place(place_to_search):
	print(term.bold(term.red("Search for any street address")))
	g = geocoders.GoogleV3()

	place_search = g.geocode(place_to_search)

	print (term.cyan(place_search))

if __name__ == '__main__':
	place(raw_input())
	