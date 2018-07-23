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
    Possible keys:
    * artist
    * artistid
    * ...
    """
    try:
        if kwargs:
            # select first key in kwargs
            key = list(kwargs.keys())[0]
            albums = _rpc.request('AudioLibrary.GetAlbums', {'filter': {key: kwargs[key]}})
        else:
            albums = _rpc.request('AudioLibrary.GetAlbums')
        return albums['albums']
    except:
        return {}


def get_songs(**kwargs):
    """
    Retrieve all songs from specified album, artist or genre
    Possible keys:
    * artist
    * artistid
    * albumid
    * ...
    """
    try:
        if kwargs:
            # select first key in kwargs
            key = list(kwargs.keys())[0]
            songs = _rpc.request('AudioLibrary.GetSongs', {'filter': {key: kwargs[key]}})
        else:
            songs = _rpc.request('AudioLibrary.GetSongs')
        return songs['songs']
    except:
        return {}