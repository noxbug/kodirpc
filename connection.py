from . import nowplaying as _nowplaying
from . import rpc as _rpc


# this file contains the connection details
global host
global port


def connect(host_='localhost', port_=8080):
    global host
    global port

    host = host_
    port = port_

    # check connection
    _rpc.ping()

    # reset now playing section
    _nowplaying.update()
