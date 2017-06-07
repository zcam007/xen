import urllib
import urllib2
from bs4 import BeautifulSoup
import Virtual1
import webbrowser

textToSearch = song_name
#print song_name
query = urllib.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)
links=[]
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    #print 'https://www.youtube.com' + vid['href']
    links.append('https://www.youtube.com' + vid['href'])
#print links[0]
webbrowser.open_new_tab(links[0])

