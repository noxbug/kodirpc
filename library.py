from . import rpc as _rpc


def update():
    """
    Cleans the library from non-existent items
    Scans the audio sources for new library items
    """
    print('Clean library...')
    _rpc.request('AudioLibrary.Clean')
    _rpc.request('VideoLibrary.Clean')
    print('Scan for new library items...')
    _rpc.request('AudioLibrary.Scan')
    _rpc.request('VideoLibrary.Scan')
    print('Library update complete')

