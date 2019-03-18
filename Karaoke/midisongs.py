from bs4 import BeautifulSoup
import os
import errno
import string
import urllib

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

with open("basi_karaoke.html", "r") as request:
    text = ''
    for line in request:
        text += line


count = 0
path = ''
for i in range(len(text)):
    # Cerca "foldheader"
    if text[i:i+len('foldheader')] == 'foldheader':
        cartella = ''
        i += len('foldheader') + 5
        while(text[i]!='>'):
            i += 1
        i += 1
        while(text[i]!='<'):
            cartella += text[i]
            i += 1
        path = "D:/midi/" + cartella
        path=path.replace('"', '')
        make_sure_path_exists(path)
        # Crea la cartella con il nome salvato
    elif text[i:i+len('href')] == 'href':
        # CERCO L'URL DEL MIDI
        while text[i]!='"':
            i += 1
        i += 1
        song_url = 'http://www.vittoriain.it/'
        while text[i]!='"':
            song_url += text[i]
            i += 1
        song_url=song_url.replace(' ', '%20')

        # CERCO IL NOME DEL MIDI
        song_name=''
        while text[i]!='>' :
            i += 1
        i += 1
        while text[i]!='<':
            song_name += text[i]
            i += 1
        indirizzo=path+'/' + song_name + '.mid'
        try:
            urllib.request.urlretrieve(song_url, indirizzo)
            #print(indirizzo)
        except:
            print(song_url)
            count+=1

 #       while text[i:i+len('</ul>')] != '</ul>':
 #           while text[i:i+len('href')] != 'href':    
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