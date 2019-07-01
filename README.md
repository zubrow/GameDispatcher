# GameDispatcher
Script for dispatching information between a gameengine and players, via stdin and stdout


Usage :
python3 GameDispatcher.py config.cfg

config.cfg is a config file containing on the first line the command for game engine execution, then on each other lines, the command for player IA execution.


Example, in bombernman.cfg
```
python3 BombermanGE.py
python3 BombermanPlayer.py
python3 BombermanPlayer.py
python3 BombermanPlayer.py
python3 BombermanPlayer.py
```
It mean that we use `python3 BombermanGE.py` as game engine, then 4 instances of `python3 BombermanPlayer.py` as players IA.
