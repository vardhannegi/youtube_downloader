from bs4 import BeautifulSoup
from pytube import YouTube
import urllib.request
import time
import os


## list of link parsed by bs4
s = []


## to name and save the playlist folder and download path respectively 
savePath = str(input("Paste your download path here: "))
directory = str(input("Write the folder name for downloading playlist: "))
path = os.path.join(savePath, directory)


## link parser
past_link_here = str(input("Paste your link here: "))
html_page = urllib.request.urlopen(past_link_here)
x = html_page.read()
soup = BeautifulSoup(x, 'html.parser')
for link in soup.findAll('a'):
    k = link.get('href')
    if 'watch' in k:
        s.append(k)
    else:
        pass


## to create playlist folder
def create_project_dir(x):
    if not os.path.exists(x):
        print('Creating directory ' + x)
        os.makedirs(x)
create_project_dir(path)


## downloading videos by using links from list s = []
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
            print(k + ' is downloading....')
            l.download(path)
            time.sleep(1)
            print('downloading compleat')

##    except Exception:
##        print('error')

    except KeyError as e:
        print('KeyError') % str(e)
