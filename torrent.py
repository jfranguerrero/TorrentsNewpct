# -*- coding: utf-8 -*-
import sys
import requests
from bs4 import BeautifulSoup
from os.path import basename
import feedparser
import datetime
from time import mktime

rss = feedparser.parse('http://feeds2.feedburner.com/newpctorrent')
now = datetime.datetime.now()
for post in rss.entries:
    dt = datetime.datetime(*post.published_parsed[:6])
    if dt.day == now.day-1:
        ignorar = post.title.count('Latino')
        ignorar2 = post.title.count('V.O.')
        ignorar3 = post.title.count('BluRay')
        if(ignorar==0 and ignorar2==0 and ignorar3==0):
            print post.title

            url=post.link
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            req = requests.get(url, headers=headers)

            statusCode = req.status_code

            if statusCode == 200:
                soup = BeautifulSoup(req.text, "lxml")
                datos2=soup.find_all('a', {'class' : 'external-url'})
                for link in datos2:
                    filename=basename(link.get('href'))
                    torrent = requests.get(link.get('href'))
                    with open("/home/"+filename, "wb") as code:
                        code.write(torrent.content)
