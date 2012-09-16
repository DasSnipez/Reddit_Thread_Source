import requests
from bs4 import BeautifulSoup
import re
import time
from easygui import *
import webbrowser


new = 2
msgbox("Welcome to Reddit Comment Counter!")
textbox("Info","info","When new comments are posted the command line will dispaly 'New Comments' and a link will be given.")
reply = enterbox(msg="Enter thread URL")



url = reply
payload = {"user_agent":"DasSnipezCommentCounter"}
def get_comments1():
    global payload
    global list1
    r = requests.get(url,params=payload)
    soup = BeautifulSoup(r.text)
    easy_soup = soup.prettify()

    comments = re.search("\d{1,5} comments",easy_soup)
    g = comments.group(0)
    number = re.sub(" comments",'',g)

    intnum = int(number)

    list1 = [0]

    list1[0] = intnum
    print list1[-1]
def get_comments2():
    global payload
    global list2
    r = requests.get(url,params=payload)
    soup = BeautifulSoup(r.text)
    easy_soup = soup.prettify()

    comments = re.search("\d{1,5} comments",easy_soup)
    g = comments.group(0)
    number = re.sub(" comments",'',g)

    intnum = int(number)
    list2 = [0]

    list2[0] = intnum
    print list2[-1]
def compare():
    if list1[-1] == list2[-1]:
        pass
    elif list2[-1] > list1[-1]:
        print "New comments."
        if ccbox("Open new page?","New Comments"):
            open_page()
        else:
            run()
    elif list1[-1] < list2[-1]:
        print "Someone deleted a comment."

def open_page():
    global url
    global new
    newurl = url + "?sort=new"
    webbrowser.open(newurl,new=new)

def run():
    get_comments1()
    time.sleep(3)
    get_comments2()
    compare()

while 1 == True:
    run()
