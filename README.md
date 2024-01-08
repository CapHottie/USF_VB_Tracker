# USF_VB_Tracker
## Dev Notes 
These are not written in the order in which they become important, rather whenever they come up in real time.

My initial goal of having a pretty highly interactive user interface was foiled by the fact that I'll have to sacrifice how stylish it will be for the sake of efficiency and time spent in the project altogether. The main reason I took on this project is because I wanted to apply my knowledge of Python, OOP, DSA, and how well I can learn to use API and other libraries. With this in mind, I set out to program this entire thing with only Python as opposed to incorporating frameworks (even if Django would be appropriate, it still comes with the hassle of HTML, JS, etc.) which meant using libraries like Tkinter. When looking for what libraries I could use to code the front-end, the one that looked the most appealing was PyQt5 since it allowed for more modern-looking GUI; however, it quickly became an issue when the main way PyQt designed interfaces was through a drag-and-drop approach which just didn't align with the challenges and learning outcomes I set for myself. Therefore, I'm currently opting for Tkinter since it seems more appropriate as I have more control over the design that way as opposed to just letting a separate program do it for me. 

I just found about the @dataclass utility which will help with the Player implementation.

### Personal Background
Last time I coded in Python was 2018/19, since I've done most of my work in Java and C, with a personal preference for C. 
## Structure notes
Big picture: There will be a game instance where most of the user interaction will take place. Outside of that, there will be data maintained and queried for all game instances likely stored in a local csv file
Very likely there will be three data frames: (1) game stats where each row is a snapshot description of an event (2) Team-level stats sheet (3) game-level player performance/actions

I keep switching between whether each of these functions will be worked on by separate python scripts or to just put everything in a single Karl file. As of 1:31 AM on 1/8/2024 I'm changing to having multiple scripts to minimize class separations and just being able to use global  variables.


## Functions:
1.- Record stats
2.- Check rotation is valid (dobutful)
3.- Calculate and display secondary/tertiary stats like hit pct and hitting efficiency

