# fandom.py
# This script is not the final version. It's only for testing purpose.

# Library
# Install dependencies with "pip3 install beautifulsoup4 requests"
import requests
import sys
import os
from bs4 import BeautifulSoup

# Variables
url = ""

# Basic argument parsing
# Bugs included, lol.
try:
	url = sys.argv[1]
except:
	print("[] Error: No URL found. Exiting")
	exit()
if "fandom" not in url.split("."):
	print("[] Error: No wiki page. Exiting")
	exit()
if "wiki" not in url.split("/"):
	print("[] Error: Page format not supported. Exiting")
	exit()

# wiki data
wikiRaw = requests.get(url+"?action=edit")
wikiTitle = url.split("/")[-1]
wikiParsed = BeautifulSoup(wikiRaw.text, 'html.parser')
path = os.path.join(os.getcwd(), wikiTitle + ".txt")

# show wiki data to user
print("[] Wiki info")
print("\ttitle:", wikiTitle)
print("\turl  :", url)
print("\tpath :", path)

# Write file
file = open(path, "w+", encoding="utf-8")
wikitext = wikiParsed.find("textarea", {"id": "wpTextbox1"})
file.write(wikitext.text)
file.close()

#  Bye