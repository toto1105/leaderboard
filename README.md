# leaderboard Project
## by Toto1105
a standard leaderboard for shooter games using buttons
This program uses the Python Tkinter library to make a "fps" kind of leaderboard. 

At this moment in time there is only one team with 7 players. Work is going on to add a second team with equal players.

##Requirements:
  - Python 3 IDLE 
  - Tkinter library
  
## Usage:
 to use it you run it in a python 3 IDLE, once you have run it you get two different options:
- write '1'. This option will give you a gamemode that will give each player 1 life. So if they die they can not respawn
- write '2'. This option will give you a gamemode that will give each player unlimited lives, so you can respawn the players.

There will be two buttons on your screen per player, one to add a kill to the counter and one to add a death to the counter or to remove the player from the game
There are also three different classes; "Assault", "Heavy" and "Officer". This can be changed in the code by going to 
```
#variables players and ranks team 1
player1 = "player 1"
player2 = "player 2"
player3 = "player 3"
player4 = "player 4"
player5 = "player 5"
player6 = "player 6"
player7 = "player 7"

rank_p1 = "Assault"
rank_p2 = "Assault"
rank_p3 = "Assault"
rank_p4 = "Assault"
rank_p5 = "Heavy"
rank_p6 = "Heavy"
rank_p7 = "Officer"
```
at the top of the program and changing the names of the ranks. The names of the players can also be changed here as well.

## Todo:
1. Add second team
2. In single life gamemode, make it that you can not add kills
3. maybe at more players and classes
4. make it easier to change the player names and classes

If anyone ever reads this and wants to use it, feel free to take it

Have a good one,
Toto1105
