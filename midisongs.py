import urllib
from bs4 import BeautifulSoup
import os
import errno
import time
import string

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

with urllib.request.urlopen("http://www.vittoriain.it/basi_karaoke.htm") as request:
    temp=request.read()
    soup=BeautifulSoup(temp, 'html.parser')
count = 0
canzoni = [tuple([ele['href'], ele.text]) for ele in soup.body.find_all('table')[5].find_all('a')]

for cartella, titolo in canzoni:
    path='D:/midi/'+cartella.split('/')[1]
    make_sure_path_exists(path)
    url = 'http://www.vittoriain.it/'+cartella
    url=url.replace(' ', '%20')
    try:
        urllib.request.urlretrieve(url, path+'/'+titolo+'.mid')
    except:
        print(url)
        count+=1
print(count)
    
#urllib.request.urlretrieve
#print(soup.body.find_all('table')[5].find_all('a')[0]['href'])
#url = 'http://www.vittoriain.it/midi/richieste/AC-DC--Thunderstruck-1990.mid'
#urllib.request.urlretrieve(url, 'D:/midi/Ac Dc - Thunderstruck.mid')
#print(soup.body.find_all('table')[5].find_all('a')[1]['href'])
#print(soup.body.find_all('table')[5].find_all('a')[1].text)
#urllib.request.urlretrieve("http://www.vittoriain.it/"+soup.body.find_all('table')[5].find_all('a')[1]['href'], 'a.mid')  