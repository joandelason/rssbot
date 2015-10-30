# rssbot

Python bot that downloads news from any RSS feed, converts them to docx format after striping all HTML and ads clutter -sth. like the Safari Reader mode- and organizes them chronologically in folders according to the posts' publishing date. 

##Use cases: 
- keep track of any hot topic in an organized way (like Bitcoin).
- compare news coming from different media
- create an archive of news diggests

Maybe journalists will find it useful if there is no better (and free) tool.

##Current features:
- scrape from a list of RSS feeds
- ads and HTML clutter removal
- docx conversion
- chronological organization in folders

##Nice to have:
- add tests
- pass as arguments, do not touch code
- improve docx formatting (bold, italics, etc)
- add the post's main image (if any)
- PDF conversion
- add tags feature to be able to organize them by topic
- add GUI to set up bot (feed's URL, refresh frequency, root location, ...)

##Usage:
Just type on the command line:

python newsbot.py

You will need to change the feeds list in the code according to your interests.
