from . import rpc as _rpc


def set_fullscreen():
    """Toggle fullscreen/GUI"""
    _rpc.request('GUI.SetFullscreen')
