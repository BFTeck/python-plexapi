from plexapi.myplex import MyPlexAccount
username  =input('Votre username:')
password = input('Votre password:')



account = MyPlexAccount(username, password)

print("Liste des serveurs: ")
for ressour in account.resources():
    print(ressour.name)

servername =input('Quel serveur ?')

plex = account.resource(servername).connect()  # returns a PlexServer instance

for sec in plex.library.sections():
    print(sec.name)

section = input('Quelle section ?')

movies = plex.library.section(section)
for video in movies.search(unwatched=True):
    print(video.title)

film =input('Quel film ?')

todownload = plex.library.section(section).get(film)

todownload.download()