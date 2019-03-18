from bs4 import BeautifulSoup
import os
import errno
import string

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

with open("basi_karaoke.htm", "r") as request:
    temp = ''
    for line in request:
        temp += line
    soup = BeautifulSoup(temp, 'lxml')
    print(soup)

#with open('prova', 'w') as f:
#    f.write(str(soup.body.find_all('table')[5]))

columns = soup.body.find_all('table')[5].tr.find_all('td')
# vedi l'html, sto facendo in modo che in columns ci sia nome cartella, nome file e directory
count = 0

# aspe ti sto chiamando, che senò non capisco un cazzo
# su 'li' ci sta il nome della cartella, in 'ul' ci sta il link e il nome del file
for column in columns:
    for folder_name, songs in zip(column.find_all('li', id='foldheader'), column.find_all('ul', id='foldinglist')):
        print('D:/midi/'+folder_name.font.text + '\n')

"""
    for cartella, titolo in canzoni:
        # Questo qui sotto si deve cambiare, ma non so come
        canzoni = [tuple([ele['href'], ele.text]) for ele in soup.body.find_all('table')[5].find_all('a')]
        # ^^^
        
        path='D:/midi/'+cartella.split('/')[1]
        make_sure_path_exists(path)
        url = 'http://www.vittoriain.it/'+cartella
        url=url.replace(' ', '%20')
        try:
            urllib.request.urlretrieve(url, path+'/'+titolo+'.mid')
        except:
            print(url)
            count+=1"""
    
#urllib.request.urlretrieve
#print(soup.body.find_all('table')[5].find_all('a')[0]['href'])
#url = 'http://www.vittoriain.it/midi/richieste/AC-DC--Thunderstruck-1990.mid'
#urllib.request.urlretrieve(url, 'D:/midi/Ac Dc - Thunderstruck.mid')
#print(soup.body.find_all('table')[5].find_all('a')[1]['href'])
#print(soup.body.find_all('table')[5].find_all('a')[1].text)
#urllib.request.urlretrieve("http://www.vittoriain.it/"+soup.body.find_all('table')[5].find_all('a')[1]['href'], 'a.mid')  

# INIZIO SPAZIO MIO
#Allora prima di tutto mi serve il nome delle cartelle come sta scritto sul sito
#comunque i link possono stare solo su quella tabella ahahahahah


# come hai fatto a capire che alcune non le scaricava
# allora ci conviene prima vedere il fatto delle cartelle cosi possiamo confrontare
# ci possiamo prendere le colonne una ad una
# su table.tbody.tr ci stanno 4 td che sono le colonne delle cartelle
# FINE SPAZIO MIO


# MARCO
#non credevo di spostare anche il tuo cursore
#cista
# Ah, quindi i link sono tutti li, chissà perché a me non scarica
# In realtà non ne sono sicuro ma mi sembravano poche
# Ok si, sono solo 28 cartelle
# Neanche metà della prima colonna praticamente
# Comunque liveshare funziona da dio
# Vai, cambia il codice
# Che io non riesco neanche a capire che c'è scritto