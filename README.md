# kodirpc
The kodirpc library is a python3 wrapper for the Kodi JSON-RPC API (https://kodi.wiki/view/JSON-RPC_API/v8).
It is by no means complete.
Features will be implemented when needed.
The RPC module performs most of the heavy lifting. 
The kodirpc library uses a separate module for every namespace in the Kodi JSON-RPC API. 
This maskes it possible to call methods using the python dot notation. 

## Usage
The example below shows how to use the library.
```python
import kodirpc as kodi

kodi.connection.connect('localhost')

kodi.player.play_pause()
kodi.input.home()
kodi.library.update()
```

The nowplaying module contains information (i.e. title, artist, album,...) 
about the currently played item. 
The auto update service tries to keep this information up to date.
However, if multiple remote applications are used, this can not be guaranteed.

## Extend the kodirpc library
Kodi's JSON-RPC API has been designed to be self-documented. 
The following example shows how to obtain a response containing a documentation 
for all the available methods and data types.
```python
documentation = kodi.rpc.help('Player.Stop')
```


