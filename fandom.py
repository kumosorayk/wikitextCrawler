import requests
import sys
import os
from bs4 import BeautifulSoup

url = ""

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


wikiRaw = requests.get(url+"?action=edit")
wikiTitle = url.split("/")[-1]
wikiParsed = BeautifulSoup(wikiRaw.text, 'html.parser')

path = os.path.join(os.getcwd(), wikiTitle + ".txt")

print("[] Wiki info")
print("\ttitle:", wikiTitle)
print("\turl  :", url)
print("\tpath :", path)

file = open(path, "w+", encoding="utf-8")
wikitext = wikiParsed.find("textarea", {"id": "wpTextbox1"})
print(wikitext)
file.write(wikitext.text)
file.close()