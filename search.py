# example request format
# https://alpine.atlassian.net/wiki/dosearchsite.action?queryString=install

import sys
import urllib
import requests
from bs4 import BeautifulSoup

# get search query from the command line
query = sys.argv[1]
root = "https://alpine.atlassian.net"
# request
base_url = "https://alpine.atlassian.net/wiki/dosearchsite.action?queryString="
exclude_spaces = ['DOC', 'CD']
# formatting for wiki
exclude_spaces = [space + '/' for space in exclude_spaces]
# if any(ext in url_string for ext in extensionsToCheck):
#    print(url_string)

# quote_plus is used to transform entities like spaces into %20
url = base_url+urllib.quote_plus(query)
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all("a", class_="search-result-link"):
    page = link.get('href')
    title = link.get_text()
    # looks if anything is in the excluded spaces
    if not any(space in page for space in exclude_spaces):
        print title
        print root+page
