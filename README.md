# BlockBuilder

![Minecraft Image](https://i.imgur.com/JYylOMj.png)

BlockBuilder is an improved, modularized version of [Fogleman's Python/Pyglet Minecraft](https://github.com/fogleman/Minecraft) with multiplayer capabilities.

The pyglet library must be installed into order to run. Use pip to install pyglet.

To run in single player (offline mode):
```
python3 main.py -s
```
To join a server:
```
python3 main.py -m <ip> <port>
```

To start your own server:
```
python3 server.py <port>
```

How to Play:
| Keystroke | Description 
| --------- | ----------- |
| W,S,A,D | Move Player |
| Space-bar | Jump |
| Tab | Enter/exit flying mode |
| Left-Click | Remove block | 
| Right-Click | Place block |
| Keys 1-5 | Change block type (note that stone blocks can't be destroyed) |


## Changes that I would like to see incorporated
- Better terrain generation
- The addition of other blocks including water and trees
- An inventory system
- A method of saving the game state
- The ability to see player positions on the server
- Refactor the server. The server is currently only being used to send information to clients when a client performs an action. If client A starts a server, modifies the world, and then client B joins the server, client B will not see the changes made by client A. In addition, if a client leaves and then joins a server, the world will be reset on their end but not other clients. I would want the server to be refactored such that world state can be saved on the server or retrieved from the host when requested.
