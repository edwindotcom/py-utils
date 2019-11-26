# 
# Usage: python pollForTag.py https://example.com

import schedule
from urllib2 import urlopen
import sched, time
from time import gmtime, strftime
import lxml.html
import sys

url = "https://example.com"
search_tag = 'title'

if len(sys.argv) == 2:
    url = sys.argv[1]

if len(sys.argv) == 3:
    search_tag = str(sys.argv[2])

print ("Polling URL: {}".format(url))

count = 0
def check_title():
    global count
    # add query string param to bust any caching
    target_url = "{}?{}".format(url, str(count))
    tree = lxml.html.parse(urlopen(target_url))
    now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    count = count + 1
    try:
        pi = tree.xpath("//{}".format(search_tag))[0] 
        print (now + " : " + pi.text)
    except:
        print(now + ' : {} not found'.format(search_tag))

schedule.every(1).second.do(check_title)

while True:
    schedule.run_pending()
