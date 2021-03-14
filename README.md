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

HOW TO PLAY:
| Keystroke | Description 
| --------- | ----------- |
| W,S,A,D | Move Player |
| Space-bar | Jump |
| Tab | Enter/exit flying mode |
| Left-Click | Remove block | 
| Right-Click | Place block |
| Keys 1-5 | Change block type (note that stone blocks can't be destroyed) |
