from bs4 import BeautifulSoup
import requests
import re
from bs4 import Comment

def prntall():
    global complete, unq_tags, urls, comments
    print('-------------URLs found on Your Website-------------------')
    for cm in complete:
        print(cm)
    print("                                                            ")

    print('-------------Tags found on Your Website-------------------')
    for tg in unq_tags:
        print(tg)
    print("                                                            ")

    print('-------------SubDomains found on Your Website-------------------')
    for rl in urls:
        print(rl)
    print("                                                            ")

    print('-------------Comments found on Your Website-------------------')
    for c in comments:
        print(c)
    print("                                                            ")

def task5():
    global complete, unq_tags, urls, comments

    domain = input("please enter the domain u want to filter in form of domain.com: ")
    fldomain ="http://www."+domain

    resp = requests.get(fldomain)

    src = resp.content

    soup = BeautifulSoup(src , "lxml")

    urls = []
    links = soup.find_all('a')

    complete = [a.get('href') for a in soup.find_all('a', href=True)]

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))


    for link in links: 
        if domain in link.attrs['href']:
            s = link.attrs['href'][:link.attrs['href'].index(domain)]
            obj=re.compile(r'http://|https://(\w.+).')
            url = obj.findall(s)
            lsurl = list(url)
            urls.append(lsurl)

    prntall()
            
