# GameDispatcher
Script for dispatching information between a gameengine and players, via stdin and stdout


## Usage 
The command line should be : 
```
python3 GameDispatcher.py config.cfg
```
config.cfg is a config file containing on the first line the command for game engine execution, then on each other lines, the command for player AI execution.


Example, in bombernman.cfg : 
```
python3 BombermanGE.py
python3 BombermanPlayer.py
python3 BombermanPlayer.py
python3 BombermanPlayer.py
python3 BombermanPlayer.py
```
It mean that we use `python3 BombermanGE.py` as game engine, then 4 instances of `python3 BombermanPlayer.py` as players AI.


## Communication
Communication between game engine and AI is done using standard input and output.

### General structure of messages
Messages have always the same structure : 
- they start with a line _`START` **`<label>`**_
- they contain as many lines as necessary
- they end with a line _`STOP` **`<label>`**_

**`<label>`** represents the label/type of message to send.


### Message flow
A game has always the same flow of messages :

At start :
1. **dispatcher** send the number of players to the **game engine**
2. **dispatcher** send to each **AI** its player number (starting at 1)
3. **game engine** send its settings to **dispatcher**
4. **dispatcher** send the settings to each **AI** 

Then, until the end, at each turn (numbered starting at 1), and for each **AI** : 
* **game engine** send the game states infos for the **AI** to the **dispacher** 
* **dispatcher** send the  game states infos to the **AI**
* **AI** send its instructions to the **dispatcher**
* **dispatcher** send the instructions to the **game engine**

### Game engine protocol 
From the game engine's point of view, communication is :
1. read a message *`<players>`* containing the number of players
2. send a message *`<settings>`* containing all the information for the comprehension of the game
3. for each turn, for each player, until the end of the game : 
  * send a message <turn #turn #player>
  * read a message <action #turn #player>

### AI protocol
From the AI's point of view, communication is :
1. read a message *`<player>`* containing the id of the player
2. read a message *`<settings>`* containing all the information for the comprehension of the game
3. for each turn, until the end of the game : 
  * read a message <turn>
  * send a message <action>
