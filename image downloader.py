#PROGRAM TO EXTRACT THE LINKS OF ALL THE IMAGES ON A WEBSITE
import urllib
import re
print "enter the url of a website "
url=raw_input(">>>")
website=urllib.urlopen(url)
html=website.read()
pattern=r'<img src=\"(.*?)\"'
pattern=re.compile(pattern)
links = re.findall(pattern,str(html))
print "enter the filename "
file=raw_input(">>>")
myfile=open(file,"w")
print "LINKS OF IMAGES"
for links in links:
	print url,links
	l=url+links
	myfile.write(str(l))
print "all the links have been copied to "+str(file)
myfile.close()



















