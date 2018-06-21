# Do not import in __init__.py
from . import player as _player


def select():
    """Select properties base on content type"""
    player = _player.get_active_player()
    if player['type'] == 'audio':
        properties = ['title', 'artist', 'album', 'duration', 'thumbnail', 'file', 'fanart']
    elif player['type'] == 'video':
        properties = ['title', 'season', 'episode', 'duration', 'showtitle', 'tvshowid', 'thumbnail', 'file', 'fanart']
    else:
        properties = ['title', 'album', 'artist', 'season', 'episode', 'duration', 'showtitle', 'tvshowid', 'thumbnail',
                      'file', 'fanart', 'streamdetails']
    return properties