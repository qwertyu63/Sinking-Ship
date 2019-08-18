# Sinking-Ship
A simple Yahtzee-like dice game programmed in Python.

This entire project is just an excuse for me to learn new tools in Python. In this case, the main tool I've learned is Tkinter... which is very useful.

# Screenshot
![Image of Sinking Ship](https://github.com/qwertyu63/Sinking-Ship/blob/master/SinkingShipImage.png)

# How to Play
Just run the Python code. Tkinter is required. Click the Help button in game for further instructions or read them mirrored below.

You will roll and reroll 6 dice.  
Click the dice you want to keep and click Reroll.  
Click a score field to Bank your current roll total as points.  
Every time you Bank, you gain 2 more rerolls (max 9).  
Each field can only be used once, so plan wisely.  
If you reach 0 rerolls and can't bank, the game ends.  
Get the highest score you can.

# Field Breakdown
Each of the 15 score fields has a different scoring condition. For convience, I will list all of them here. A set of dice is a collection of dice with the same number; seperate sets must be different numbers from each other.

-- Pair: Contains a set of at least two dice.  
-- Three of a Kind: Contains a set of at least three dice.  
-- Four of a Kind: Contains a set of at least four dice.  
-- Five of a Kind: Contains a set of at least five dice.  
-- Six of a Kind: Contains a set of six dice.  
-- Two Pair: Contains two seperate sets of at least two dice each.  
-- Three Pair: Contains three seperate sets of two dice each.  
-- Full House: Contains two seperate sets; one must be at least three dice, the other at least two dice.  
-- Double Trips: Contains two seperate sets of at three dice each.  
-- Four and Pair: Contains two seperate sets; one must be four dice, the other two dice.  
-- Three in a Row: Contains three consecutive numbers (123, 234, 345 or 456).  
-- Four in a Row: Contains four consecutive numbers (1234, 2345 or 3456).  
-- Five in a Row: Contains five consecutive numbers (12345 or 23456).  
-- Six in a Row: Contains one of each number (123456).  
-- Wild: Any combination.  
