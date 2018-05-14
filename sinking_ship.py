from tkinter import *
from tkinter import messagebox
from random import randint
from collections import Counter
window = Tk()
window.title("Sinking Ship")
window.geometry('400x230')

dice = [None,None,None,None,None,None]
die = [None,None,None,None,None,None]

die[0] = Button(window, text="[]", command= lambda:switch(0), bg = "white")
die[0].grid(column=1, row=1)
die[1] = Button(window, text="[]", command= lambda:switch(1), bg = "white")
die[1].grid(column=1, row=2)
die[2] = Button(window, text="[]", command= lambda:switch(2), bg = "white")
die[2].grid(column=1, row=3)
die[3] = Button(window, text="[]", command= lambda:switch(3), bg = "white")
die[3].grid(column=1, row=4)
die[4] = Button(window, text="[]", command= lambda:switch(4), bg = "white")
die[4].grid(column=1, row=5)
die[5] = Button(window, text="[]", command= lambda:switch(5), bg = "white")
die[5].grid(column=1, row=6)

holds = [False,False,False,False,False,False]

def switch(index):
    global holds
    global dice
    holds[index] =  not holds[index]
    update_dice(dice)

scores = {"Pair": 0, "Three of a Kind": 0, "Four of a Kind": 0,
"Five of a Kind": 0, "Six of a Kind": 0, "Two Pair": 0, 
"Three Pair": 0, "Full House": 0, "Double Trips": 0, 
"Four and Pair": 0, "Three in a Row": 0, "Four in a Row": 0,
"Five in a Row": 0, "Six in a Row": 0, "Wild": 0}

def dice_counter(rolls):
    hold = Counter(rolls)
    result = []
    for i in range(1,7):
        result.append(hold.get(i, 0))
    return result

def sets_counter(counts):
    hold = sorted(counts, reverse=True)
    sets = []
    if hold[0] >= 2:
        sets.append("Pair")
        if hold[1] >= 2:
            sets.append("Two Pair")
            if hold[2] >= 2:
                sets.append("Three Pair")
    if hold[0] >= 3:
        sets.append("Three of a Kind")
        if hold[1] >= 2:
            sets.append("Full House")
        if hold[1] >= 3:
            sets.append("Double Trips")
    if hold[0] >= 4:
        sets.append("Four of a Kind")
        if hold[1] >= 2:
            sets.append("Four and Pair")
    if hold[0] >= 5:
        sets.append("Five of a Kind")
    if hold[0] >= 6:
        sets.append("Six of a Kind")
    runs = run_counter(counts)
    if runs >= 3:
        sets.append("Three in a Row")
    if runs >= 4:
        sets.append("Four in a Row")
    if runs >= 5:
        sets.append("Five in a Row")
    if runs >= 6:
        sets.append("Six in a Row")
    sets.append("Wild")
    sets = field_strip(sets)
    return sets

def field_strip(fields):
    global scores
    hold = []
    for x in fields:
        if scores[x] == 0:
            hold.append(x)
    return hold

def run_counter(counts):
    streak = 0
    array = []
    for item in counts:
        if item == 0:
            array.append(streak)
            streak = 0
        else:
            streak += 1
    array.append(streak)
    return max(array)

def update_dice(dice):
    global die
    for n, i, lock in zip(dice, die, holds):
        if lock:
            i.configure(text="X ["+str(n)+"] X", bg = "lightgrey")
        else:
            i.configure(text="["+str(n)+"]", bg = "white")

def roll_dice():
    pool = []
    relock = []
    global dice
    global holds
    for die, hold in zip(dice, holds):
        if hold == True:
            pool.append(die)
            relock.append(die)
        else:
            pool.append(randint(1,6))
    dice = sorted(pool)
    for n in range(0,6):
        holds[n] = False
    for n, i in zip(dice, range(0,6)):
        if n in relock:
            holds[i] = True
            relock.remove(n)
    return sorted(pool)

rerolls = 2

def end_game(start):
    global scoreboard
    global scores
    global reset_trigger
    for item, label in zip(scores,scoreboard):
        label.configure(text=item + ": " + str(scores[item]))
        label.configure(state='disabled', bg = "white")
    helpb.configure(text="Reset")
    reset_trigger = True
    final_message = start
    total_score = sum(scores.values())
    final_message += "\nFinal Score: "+str(total_score)+"\n"
    if total_score >= 350:
        final_message += "Rank S! Amazing play!"
    elif total_score >= 300:
        final_message += "Rank A+! Well played!"
    elif total_score >= 275:
        final_message += "Rank A! Well played!"
    elif total_score >= 250:
        final_message += "Rank B. Good game."
    elif total_score >= 225:
        final_message += "Rank C."
    elif total_score >= 200:
        final_message += "Rank D. Better luck next time."
    else:
        final_message +="Rank F. Better luck next time."
    messagebox.showinfo('Game Over',final_message)

def click_roll():
    global rerolls
    rolls = roll_dice()
    update_dice(rolls)
    rerolls -= 1
    reroll.configure(text="Reroll ["+str(rerolls)+"]")
    counted_dice = dice_counter(rolls)
    valid_sets = sets_counter(counted_dice)
    print_scores(valid_sets)
    if rerolls == 0:
        reroll.configure(state='disabled')
        if len(valid_sets) == 0:
            end_game("You can not score. Your ship has sunk.")

def bank(field):
    global dice
    global scores
    global rerolls
    global holds
    points = sum(dice)
    assert scores[field] == 0
    scores[field] = points
    for n in range(0,6):
        holds[n] = False
    rerolls += 3
    if rerolls >= 11:
        rerolls = 10
    click_roll()
    reroll.configure(state='normal')
    if min(scores.values()) != 0:
        end_game("Every field is full. Your ship will float.")

def print_scores(valid):
    global scoreboard
    global scores
    for item, label in zip(scores,scoreboard):
        label.configure(text=item + ": " + str(scores[item]))
        if item in valid:
            label.configure(state='normal', bg = "lightyellow")
        else:
            label.configure(state='disabled', bg = "lightgrey")
        if scores[item] != 0:
            label.configure(state='disabled', bg = "white")
    dietotal.configure(text="Roll Total: " + str(sum(dice)))
    currentscore.configure(text="Total Score: " + str(sum(scores.values())))

reroll = Button(window, text="Reroll [2]", command=click_roll)
reroll.grid(column=1, row=8)

window.grid_columnconfigure(0, minsize=10)
window.grid_columnconfigure(2, minsize=20)
window.grid_rowconfigure(0, minsize=10)
window.grid_rowconfigure(6, minsize=20)

scoreboard = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
scoreboard[0] = Button(window, text="---", command= lambda:bank("Pair"))
scoreboard[0].grid(column=3, row=1)
scoreboard[1] = Button(window, text="---", command= lambda:bank("Three of a Kind"))
scoreboard[1].grid(column=3, row=2)
scoreboard[2] = Button(window, text="---", command= lambda:bank("Four of a Kind"))
scoreboard[2].grid(column=3, row=3)
scoreboard[3] = Button(window, text="---", command= lambda:bank("Five of a Kind"))
scoreboard[3].grid(column=3, row=4)
scoreboard[4] = Button(window, text="---", command= lambda:bank("Six of a Kind"))
scoreboard[4].grid(column=3, row=5)

scoreboard[5] = Button(window, text="---", command= lambda:bank("Two Pair"))
scoreboard[5].grid(column=4, row=1)
scoreboard[6] = Button(window, text="---", command= lambda:bank("Three Pair"))
scoreboard[6].grid(column=4, row=2)
scoreboard[7] = Button(window, text="---", command= lambda:bank("Full House"))
scoreboard[7].grid(column=4, row=3)
scoreboard[8] = Button(window, text="---", command= lambda:bank("Double Trips"))
scoreboard[8].grid(column=4, row=4)
scoreboard[9] = Button(window, text="---", command= lambda:bank("Four and Pair"))
scoreboard[9].grid(column=4, row=5)

scoreboard[10] = Button(window, text="---", command= lambda:bank("Three in a Row"))
scoreboard[10].grid(column=5, row=1)
scoreboard[11] = Button(window, text="---", command= lambda:bank("Four in a Row"))
scoreboard[11].grid(column=5, row=2)
scoreboard[12] = Button(window, text="---", command= lambda:bank("Five in a Row"))
scoreboard[12].grid(column=5, row=3)
scoreboard[13] = Button(window, text="---", command= lambda:bank("Six in a Row"))
scoreboard[13].grid(column=5, row=4)
scoreboard[14] = Button(window, text="---", command= lambda:bank("Wild"))
scoreboard[14].grid(column=5, row=5)

dietotal = Label(window, text="---")
dietotal.grid(column=3, row=7)
currentscore = Label(window, text="---")
currentscore.grid(column=4, row=8)

reset_trigger = False

def help_button():
    if reset_trigger:
        reset()
    else:
        messagebox.showinfo('Sinking Ship Help','''You will roll and reroll 6 dice.
Click the dice you want to keep and click Reroll.
Click a score field to Bank your current roll total as points.
Every time you Bank, you gain 2 more rerolls (max 9).
Each field can only be used once, so plan wisely.
If you reach 0 rerolls and can't bank, the game ends.
Get the highest score you can.''')

def reset():
    global dice
    global holds
    global scores
    global reset_trigger
    dice = [None,None,None,None,None,None]
    scores = {"Pair": 0, "Three of a Kind": 0, "Four of a Kind": 0,
"Five of a Kind": 0, "Six of a Kind": 0, "Two Pair": 0, 
"Three Pair": 0, "Full House": 0, "Double Trips": 0, 
"Four and Pair": 0, "Three in a Row": 0, "Four in a Row": 0,
"Five in a Row": 0, "Six in a Row": 0, "Wild": 0}
    startdice=roll_dice()
    update_dice(startdice)
    start_count = dice_counter(startdice)
    start_sets = sets_counter(start_count)
    print_scores(start_sets)
    helpb.configure(text="Help")
    reset_trigger = False

helpb = Button(window, text="Help", command=help_button)
helpb.grid(column=5, row=8)

reset()
window.mainloop()
