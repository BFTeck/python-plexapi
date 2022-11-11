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

servername = input('Quel serveur ?')
servername = account.resources()[int(servername)].name

plex = account.resource(servername).connect()  # returns a PlexServer instance
i = 0
for sec in plex.library.sections():
    print("[" + str(i) + "] " + sec.title)
    i = i + 1

section = input('Quelle section ?')
section = plex.library.sections()[int(section)].title

movies = plex.library.section(section)
i = 0
for video in movies.all():
    print("[" + str(i) + "] " + video.title)
    i = i + 1

film = input('Quel film ?')
film = movies.all()[int(film)].title

todownload = plex.library.section(section).get(film)

todownload.download()