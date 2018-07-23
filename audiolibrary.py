from . import rpc as _rpc


def clean():
    """
    Cleans the audio library from non-existent items
    """
    _rpc.request('AudioLibrary.Clean')


def scan():
    """
    Scans the audio sources for new library items
    """
    _rpc.request('AudioLibrary.Scan')


def get_artists():
    """
    Retrieve all artists. For backward compatibility by default
    this implicity does not include those that only contribute
    other roles, however absolutely all artists can be returned
    using allroles=true
    """
    try:
        artists = _rpc.request('AudioLibrary.GetArtists')
        return artists['artists']
    except:
        return {}


def get_albums(**kwargs):
    """
    Retrieve all albums from specified artist (and role) or that has songs of the specified genre
    """
    try:
        if 'artist_id' in kwargs:
            albums = _rpc.request('AudioLibrary.GetAlbums', {'filter': {'artistid': kwargs['artist_id']}})
        elif 'artist' in kwargs:
            albums = _rpc.request('AudioLibrary.GetAlbums', {'filter': {'artist': kwargs['artist']}})
        else:
            albums = _rpc.request('AudioLibrary.GetAlbums')
        return albums['albums']
    except:
        return {}


def get_songs(**kwargs):
    try:
        if 'artist_id' in kwargs:
            songs = _rpc.request('AudioLibrary.GetSongs', {'filter': {'artistid': kwargs['artist_id']}})
        elif 'artist' in kwargs:
            songs = _rpc.request('AudioLibrary.GetSongs', {'filter': {'artist': kwargs['artist']}})
        elif 'album_id' in kwargs:
            songs = _rpc.request('AudioLibrary.GetSongs', {'filter': {'album_id': kwargs['album_id']}})
        else:
            songs = _rpc.request('AudioLibrary.GetSongs')
        return songs['songs']
    except:
        return {}