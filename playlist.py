from . import properties as _properties
from . import rpc as _rpc


def add():
    """Add item(s) to playlist"""
    raise NotImplementedError


def clear():
    """Clear playlists"""
    try:
        _rpc.request('Playlist.Clear')
    except:
        pass


def get_playlists():
    """Returns all existing playlists"""
    try:
        playlists = _rpc.request('Playlist.GetPlaylists')
        return playlists
    except:
        return {}


def get_items():
    """Get all items from playlist"""
    try:
        playlists = get_playlists()
        # iterate over all playlists
        for playlist in playlists:
            items = _rpc.request('Playlist.GetItems', {'playlistid': playlist['playlistid'], 'properties': _properties.select()})
            # check if playlist is empty
            if 'items' in items:
                # append playlist type
                items['type'] = playlist['type']
                # return statement breaks loops
                return items['items']
        # all playlist empty, return empty dict
        return {}
    except:
        return {}


def get_properties():
    """Retrieves the values of the given properties"""
    raise NotImplementedError


def insert():
    """Insert item(s) into playlist. Does not work for picture playlists (aka slideshows)"""
    raise NotImplementedError


def remove():
    """Remove item from playlist. Does not work for picture playlists (aka slideshows)"""
    raise NotImplementedError


def swap():
    """Swap items in the playlist. Does not work for picture playlists (aka slideshows)"""
    raise NotImplementedError