from bs4 import BeautifulSoup
from pytube import YouTube
import urllib.request
from pathlib import Path
import time
import pprint
import re
import os
import os.path
from os import path

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

directory = 'Hacker101'
s = []
savePath = "G:/Download/video/"

html_page = urllib.request.urlopen("https://www.youtube.com/playlist?list=PLxhvVyxYRviZd1oEA9nmnilY3PhVrt4nj")
x = html_page.read()
##print(x)
soup = BeautifulSoup(x, 'html.parser')
for link in soup.findAll('a'):
    k = link.get('href')
    if 'watch' in k:
        s.append(k)
    else:
        pass

path = os.path.join(savePath, directory)
##print(path)
##os.makedirs(path)
def create_project_dir(x):
    if not os.path.exists(x):
        print('Creating directory ' + x)
        os.makedirs(x)
##    else:
##        print('File already exist')
create_project_dir(path)

##for x in s:
##    link="https://www.youtube.com" + x
##    yt = YouTube(link)
##    k = yt.title
##    j = yt.streams.filter(progressive=True).all()
##    l = yt.streams.first()
##    l.download(path)
##    print('downloading compelet')
##    time.sleep(3)
    


for x in s:
    link="https://www.youtube.com" + x
    yt = YouTube(link)
    k = yt.title
    file_path = path + '\\' + k + '.mp4'
    try:
        if os.path.exists(file_path):
            print(k + ' is \n' + "already downloaded")
        else:
            j = yt.streams.filter(progressive=True).all()
            l = yt.streams.first()
            prYellow(k + ' is downloading....')
            l.download(path)
            time.sleep(1)
            prGreen('downloading compleat')
##    except Exception:
##        prRed('error')

    except KeyError as e:
        prRed('KeyError') % str(e)



    
##s = []
###link of the video to be downloaded
##with open("youtube_links.txt", "r") as fp:
##        line = fp.readline()
##        while line:
##                x = "{}".format(line.strip())
##                line = fp.readline()
##                s.append(line)
