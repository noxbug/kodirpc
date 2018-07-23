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
    artists = _rpc.request('AudioLibrary.GetArtists')
    return artists['artists']


def get_albums(artistid=None):
    """
    Retrieve all albums from specified artist (and role) or that has songs of the specified genre
    """
    if artistid:
        albums = _rpc.request('AudioLibrary.GetAlbums',{'filter': {'artistid': artistid}})
    else:
        albums = _rpc.request('AudioLibrary.GetAlbums')
    return albums['albums']