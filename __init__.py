from . import connection
from . import rpc
from . import input
from . import player
from . import library
from . import gui
from . import nowplaying

def connect(host='localhost', port=8080):
    connection.host = host
    connection.port = port

    # check connection
    rpc.ping()

    # reset now playing section
    nowplaying.update()

