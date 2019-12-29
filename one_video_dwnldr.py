from pytube import YouTube
import time
from pytube.compat import parse_qsl

link="https://www.youtube.com/watch?v=XeltAGwwsDQ"
yt = YouTube(link)
k = yt.title
file_path = "G:/Download/video"

j = yt.streams.filter(progressive=True).all() #.filter(progressive=True)
print(j)
get_itag = str(input('select itag: '))
l = yt.streams.get_by_itag(get_itag)
print(k + ' is downloading....')
l.download(file_path)
time.sleep(1)
print('download complete')
