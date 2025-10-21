def make_album(artist_name, album_name, songs=None):
    """Return a dictionary of information about album."""
    album = {'artist': artist_name, 'album': album_name}
    if songs:
        album['songs'] = songs
    return album
artist = make_album('Maroon 5', 'Songs about Jane', songs=12)
print(artist)


def make_album(artist_name, album_name, songs=None):
    """Return a dictionary of information about album."""
    album = {'artist': artist_name, 'album': album_name}
    if songs:
        album['songs'] = songs
    return album
artist = make_album('Linken Park', 'Hybrid Theory')
print(artist)


def make_album(artist_name, album_name, songs=None):
    """Return a dictionary of information about album."""
    album = {'artist': artist_name, 'album': album_name}
    if songs:
        album['songs'] = songs
    return album
artist = make_album('Michael Jackson', 'Thriller')
print(artist)























