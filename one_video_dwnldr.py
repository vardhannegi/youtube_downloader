from pytube import YouTube
import time
from pytube.compat import parse_qsl

link= str(input("Paste your link here: "))
yt = YouTube(link)
k = yt.title
file_path = str(input("Paste your download path here: "))

j = yt.streams.filter(progressive=True).all()
print(j)
get_itag = str(input('select itag: '))
l = yt.streams.get_by_itag(get_itag)
print(k + ' is downloading....')
l.download(file_path)
time.sleep(1)
print('download complete')
