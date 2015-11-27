# rssbot

Python bot that downloads news from any RSS feed, converts them to docx format after striping all HTML and ads clutter -sth. like the Safari Reader mode- and organizes them chronologically in folders according to the posts' publishing date. 


##Screenshots

![overview](https://cloud.githubusercontent.com/assets/15065645/10857587/3c18add4-7f4f-11e5-8f20-89b1a3b52ae6.png)

![overview2](https://cloud.githubusercontent.com/assets/15065645/10857593/475027a4-7f4f-11e5-8863-1051ee427ed5.png)

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
If you found this project interesting and want to contribute, these are the main ideas that come to my mind:

- add tests
- pass RSS url and root location as arguments, do not touch code
- package the app in a bundle, so no need to install dependencies
- improve docx formatting (bold, italics, etc)
- add the post's main image (if any)
- PDF conversion
- add tags feature to be able to organize them by sub-topic (call an AI web service like IBM's Watson)
- add GUI to set up bot (feed's URL, refresh frequency, root location, ...)



##Installation:
There are several dependencies that need to be installed:
- beautifulSoup4
- docx
- readability 

##Usage:
Just type on the command line:

python newsbot.py

You may want to change the feeds list in the code according to your interests and rename the root folder.
