# kodirpc
The kodirpc library is a python3 wrapper for the Kodi JSON-RPC API (https://kodi.wiki/view/JSON-RPC_API/v8).
It is bo no means complete, but is written to be easily extendable.
The RPC module performs most of the heavy lifting. 
The kodirpc library uses a separate module for every namespace in Kodi JSON-RPC API. 
This maskes it possible to call methods using the python dot notation. 
Look at example.py to see how to use the library.