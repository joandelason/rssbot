import os, sys
import datetime, locale
from calendar import TimeEncoding, month_name
import time, threading

import rssNewsSpider


FREQUENCY_HOURS = 60*60*6 


RSS_list = [
        'http://redfivesoftware.com/AltCoin.xml',
        #'http://www.bitcoinnoticias.com/?format=feed&type=rss',
        #'https://letstalkbitcoin.com/rss/feed/blog',
        'http://thebitcoin.news/feed/',
        #'http://elbitcoin.org/feed/'
       ]

    

def refresh():
   print 'Starting bot on {0}'.format(time.ctime())
   
   start = time.time()
   addedPosts = 0
   ignoredPosts = 0
   for RSS in RSS_list:
       spider = rssNewsSpider.RssNewsSpider(RSS)
       spider.fetchNews()
       addedPosts   += spider.addedPosts
       ignoredPosts += spider.ignoredPosts
   
   end = time.time()
   hours, rem = divmod(end-start, 3600)
   minutes, seconds = divmod(rem, 60)
   
   print '\nBot finished on {0}'.format(time.ctime())
   print "Added {0} posts. Ignored {1} posts".format(addedPosts, ignoredPosts)
   print("Elapsed time: {:0>2}h {:0>2}min {:05.2f}s\n".format(int(hours),int(minutes),seconds))
   

   
   #restart again in FREQUENCY_HOURS hours
   #synchronous feature is disabled
   #threading.Timer(FREQUENCY_HOURS, refresh()).start()


refresh()

    


