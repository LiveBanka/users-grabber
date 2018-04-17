# -*- coding: utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup
import urllib2
import time


def get_pages():
    if not os.path.exists('temp'):
        os.makedirs('temp')
    for i in range(1,50):
        time.sleep(20)
        site = ('https://github.com/search?o=desc&p='+str(i)+'&q=a&s=followers&type=Users')
        page = requests.get(site)
        temp_txt=open('temp/temp'+str(i)+'.html','w+')
        temp_txt.write(page.text.encode('utf-8'))
        temp_txt.close()
        print "|DONE|" , i

def users_links():
    users_links = open('users_links.txt','w+')
    for html in os.listdir(os.path.join('temp')):
        page = urllib2.urlopen('file:///'+ os.path.abspath('temp/') + '/' + html)
        html_page = page.read()
        site = BeautifulSoup(html_page , 'html.parser')
        user_containers=site.find_all('div',{'class':'user-list-info ml-2'})
        for user in user_containers:
            users_links.write(user.a.get('href')+'\n')
            print user.a.get('href')
    users_links.close()



get_pages()
users_links()
