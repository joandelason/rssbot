# rssbot

Python bot that downloads news from any RSS feed, converts them to docx format after striping all HTML and ads clutter -sth. like the Safari Reader mode- and organizes them chronologically in folders according to the posts' publishing date. 

Use cases: 
- keep track of any hot topic in an organized way (like Bitcoin).
- compare news coming from different media

Maybe journalists will find it useful if there is no better (and free) tool.

Current features:
- read from a given RSS feed
- ads and HTML clutter removal
- docx conversion
- chronological organization in folders

Nice to have:
- read from a list of RSS feeds
- better date parsing
- pass as arguments, do not touch code
- improve docx formatting
- add the post's main image (if any)
- add GUI to set up bot (feed's URL, refresh frequency, root location, ...)
