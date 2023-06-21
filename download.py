import configparser
from plexapi.myplex import MyPlexAccount
import os.path

file_exists = os.path.exists('plexaccount.ini')

if file_exists:
    config = configparser.ConfigParser()
    config.sections()
    config.read('plexaccount.ini')
    username = config['plex.account']['User']
    password = config['plex.account']['Password']
    rep= input('Voulez vous reutiliser le compte de ' +username+' ? (Oui ou Non)')
    if rep != "Oui":
        username = input('Votre username:')
        password = input('Votre password:')
        config = configparser.ConfigParser()
        config['plex.account'] = {}
        config['plex.account']['User'] = username
        config['plex.account']['Password'] = password
        with open('plexaccount.ini', 'w') as configfile:
            config.write(configfile)


else:
    username = input('Votre username:')
    password = input('Votre password:')
    config = configparser.ConfigParser()
    config['plex.account'] = {}
    config['plex.account']['User'] = username
    config['plex.account']['Password'] = password
    with open('plexaccount.ini', 'w') as configfile:
        config.write(configfile)

account = MyPlexAccount(username, password)

print("Liste des serveurs: ")
i = 0
for ressour in account.resources():
    print("["+str(i)+"] "+ressour.name)
    i = i+1

while True:
    servername = input('Quel serveur ?')
    if not servername:
        continue
    else:
        servername = account.resources()[int(servername)].name
        break

plex = account.resource(servername).connect()  # returns a PlexServer instance
i = 0
for sec in plex.library.sections():
    print("[" + str(i) + "] " + sec.title)
    i = i + 1


while True:
    section = input('Quelle section ?')
    if not section:
        continue
    else:
        section = plex.library.sections()[int(section)].title
        break



movies = plex.library.section(section)
i = 0
for video in movies.all():
    print("[" + str(i) + "] " + video.title)
    i = i + 1


if movies.__class__.__name__ == "MovieSection":
    
    while True:
        film = input('Quel film ?')
        if not film:
            continue
        else:
            itemtodownload = movies.all()[int(film)].title 
            todownload = plex.library.section(section).get(itemtodownload)
            break
       


else:
    while True:
        series = input('Quel serie ?')
        if not series:
            continue
        else:
            series = movies.all()[int(series)].title 
            break
        
    saisons = plex.library.section(section).get(series).seasons()
    i = 1
    print("[0] Toutes ")
    for saison in saisons:
        print("[" + str(i) + "] Saison " + str(saison.index))
        i = i + 1
    
    while True:
        saisonnum = input('Quelle saison ?')
        if not saisonnum:
            continue
        else:
            todownload = plex.library.section(section).get(series).season(int(saisonnum))
            if int(saisonnum) == 0:
                todownload = plex.library.section(section).get(series)
            break

#Now download
todownload.download()