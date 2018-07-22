from . import rpc as _rpc


def get_artists():
    """
    Retrieve all artists. For backward compatibility by default
    this implicity does not include those that only contribute
    other roles, however absolutely all artists can be returned
    using allroles=true
    """
    artists = _rpc.request('AudioLibrary.GetArtists')
    return artists['artists']