from bs4 import BeautifulSoup
import urllib2

# these are the "old" docs
# input the spaces you want to exclude here
exclude_spaces = ['DOC', 'CD']
# format with slashes
exclude_spaces = [space + '/' for space in exclude_spaces]

# include the filename that has the list of urls you want to crawl
list_o_links = 'v5links'

with open(list_o_links, 'rb') as links:
    # keep count of bad links
    bad_counter = 0
    for url in links:
        try:
            data = urllib2.urlopen(url)
            # only proceed if its not a 404
            if data.getcode() == 200:
                # get the html data from the page
                data = data.read()
                page = BeautifulSoup(data, 'html.parser')
                # get the links
                for link in page.findAll('a'):
                    href = link.get('href')
                    title = link.text
                    if href is not None:
                        # find if there are any old links in there
                        # if any(space in page for space in exclude_spaces):
                        if 'DOC/' in href or 'CD/' in href:
                            bad_counter += 1
                            print "I found an old link on this page: " + url
                            print "Please change " + "\"" + title + "\"", href + "\n"
        # if there's a 404 let us know
        except urllib2.HTTPError, e:
            if e.code == 404:
                print "This url was a 404: " + url
                print "I found it on: " + url

    print "I found " + str(bad_counter) + " links to old spaces."
    # TODO output a report with bad/broken links
