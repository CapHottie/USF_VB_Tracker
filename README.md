# USF_VB_Tracker
## Background
Last time I coded in Python was 2018/19, since I've done most of my work in Java and C, with a personal preference for the latter. 
## Structure notes
Big picture: There will be a game instance where most of the user interaction will take place. Outside of that, there will be data maintained and queried for all game instances likely stored in a local csv file
Very likely there will be three data frames: (1) game stats where each row is a snapshot description of an event (2) Team-level stats sheet (3) game-level player performance/actions
## Functions:
1.- Record stats
2.- Check rotation is valid
3.- Calculate and display secondary/tertiary stats like hit pct and hitting efficiency

## Implementation:
Use PyQt5 for front, python for backend. 
