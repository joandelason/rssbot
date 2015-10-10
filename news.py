import feedparser;
import datetime, time;
from collections import namedtuple
import htmlReader, docxConverter, locale, os
from calendar import TimeEncoding, month_name


bitdaily = "http://www.bitdaily.com/taxonomy/term/1446/all/feed";



#includes the links to all posts  to avoid overwriting existing ones 
POSTS_FILE = 'posts.txt'

PostModel = namedtuple("PostModel", ['title', 'content', 'link', 'updated'])


class RssNewsSpider:
    
    def __init__(self, rssUrl):
        dom = feedparser.parse(rssUrl)
        self.news = dict()
        self.all_posts = self.getAllPostsFromFile()
        
        for post in dom.entries:
            updated = self.parse_date(post)
            
            if updated != None and not self.isPostAlreadyInPostsFile(post.link):
                self.addPostToFile(post.link)
                
                updatedDay = datetime.date(updated.tm_year, updated.tm_mon, updated.tm_mday)

                model = PostModel(post.title, '',link=post.link, updated=updatedDay)

                self.news[post.link] = model
            



    def parse_date(self, post):
        if post.updated_parsed !=None:            
            return post.updated_parsed #que objeto es ? datetime, time

        date  = post.updated.split(' ')[0]
        if date == '':
            return None
        return time.strptime(date, "%m/%d/%Y")


        
    def fetchNews(self):
        for link, postModel in self.news.iteritems():            
            reader =  htmlReader.HtmlReader(link);
            #we will set the parent path as root. Use os.getcwd()
            currentpath = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) 

            filepath = currentpath +'/' + self.get_relative_path(postModel.updated)                
            print "Adding post '" + reader.getTitle() + "' to " + filepath                
            c = docxConverter.DocxConverter( reader.getTitle(), reader.getContent(), link, filepath)
                
                

    def get_localized_month_name(self, date):
        with TimeEncoding(locale.getdefaultlocale()) as encoding:
            s = month_name[date.month]
            if encoding is not None:
                s = s.decode(encoding)
            return s.upper()


    def get_relative_path(self, date):
        t = (date.year, date.month, date.day, 0, 0, 0, 0, 0, 0)
        t = time.mktime(t)
        day_pad = time.strftime("%d", time.gmtime(t))
        month_short = time.strftime("%b", time.gmtime(t)).upper()
        year_short = time.strftime("%y", time.gmtime(t))
        day = '{0} {1} {2}'.format(day_pad, month_short, year_short)
        month = '{0} {1}'.format(self.get_localized_month_name(date), date.year)
        year = date.year;
                        
        return "{0}/{1}/{2}".format(year, month, day)
        

    def getAllPostsFromFile(self):
        links = set()
        with open(POSTS_FILE, "a+") as file:
            for line in file:
                links.add(line)
        return links
    
    
    def isPostAlreadyInPostsFile(self, link):
        if not link in self.all_posts:
            print 'discarded ' + link
            
        return link in self.all_posts
        
        
    def addPostToFile(self, link):
        with open(POSTS_FILE, "a") as file:
            file.write(link+'\n')


