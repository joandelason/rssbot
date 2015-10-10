import os, sys
import datetime, locale
from calendar import TimeEncoding, month_name
import time, threading

import news


FREQUENCY_HOURS = 60*60*6 



#RSS = 'https://www.reddit.com/r/Bitcoin/.rss'
#RSS = "http://www.bitdaily.com/taxonomy/term/1446/all/feed"
RSS = "http://redfivesoftware.com/AltCoin.xml"

    

def refresh():
   print 'Starting bot on {0}'.format(time.ctime())
   
   spider = news.RssNewsSpider(RSS)
   spider.fetchNews()
   
   print 'Bot finished on {0}\n'.format(time.ctime())
   #restart again in FREQUENCY_HOURS hours
   #synchronous feature is disabled
   #threading.Timer(FREQUENCY_HOURS, refresh()).start()


refresh()

    


