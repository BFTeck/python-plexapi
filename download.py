from plexapi.myplex import MyPlexAccount
username = input('Votre username:')
password = input('Votre password:')



account = MyPlexAccount(username, password)

print("Liste des serveurs: ")
i=1
for ressour in account.resources():
    print("["+str(i)+"] "+ressour.name)
    i = i+1

servername = input('Quel serveur ?')
servername = account.resources()[int(servername)].name

plex = account.resource(servername).connect()  # returns a PlexServer instance
i=1
for sec in plex.library.sections():
    print("[" + str(i) + "] " + sec.title)
    i = i + 1

section = input('Quelle section ?')
section = plex.library.sections()[int(section)].title

movies = plex.library.section(section)
i=1
for video in movies.all():
    print("[" + str(i) + "] " + video.title)
    i = i + 1

film =input('Quel film ?')
film = movies.all()[int(film)].title

todownload = plex.library.section(section).get(film)

todownload.download()