import urllib2 
from bs4 import BeautifulSoup
from readability.readability import Document


#Given an html document returns the text

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


url = "http://cointelegraph.com/news/115396/perfect-balance-how-exchange-alternatives-are-taking-on-the-btc-dinosaurs";



class HtmlReader:
    
    def __init__(self, url):
        self.url = url;
        req = urllib2.Request(url, headers=hdr)
        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()
        self.html = page.read();        
        self.text = Document(self.html, "lxml").summary()
    
    def getTitle(self):
        return Document(self.html, "lxml").short_title()
    
    def getContent(self):
        return BeautifulSoup(self.text, "lxml").getText()


