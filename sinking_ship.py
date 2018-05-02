from random import randint
from collections import Counter

def roll_dice(dice=6, sides=6):
    pool = []
    count = 0
    while count != dice:
        pool.append(randint(1,sides))
        count += 1
    return sorted(pool)

def dice_counter(rolls, sides=6):
    hold = Counter(rolls)
    result = []
    for i in range(1,sides+1):
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
    return sets
    
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

def reroll(rolls):
    p_f = False
    while not p_f:
        print(*rolls, sep=", ")
        hold = input("Keep (no spaces, - keeps all): ")
        if hold == "-":
            keep = rolls
            break
        keep = []
        for n in hold:
            keep.append(int(n))
        p_f = reroll_check(rolls, keep)
        if not p_f:
            print("You didn't roll that.")
    unheld = 6 - len(keep)
    rolls = roll_dice(unheld)
    rolls += keep
    return sorted(rolls)

def reroll_check(rolls, keep):
    hold = rolls
    for value in keep:
        if value in hold:
            hold.remove(value)
        else:
            return False
    return True

scores = {"Pair": 0, "Three of a Kind": 0, "Four of a Kind": 0,
"Five of a Kind": 0, "Six of a Kind": 0, "Two Pair": 0, 
"Three Pair": 0, "Full House": 0, "Double Trips": 0, 
"Four and Pair": 0, "Three in a Row": 0, "Four in a Row": 0,
"Five in a Row": 0, "Six in a Row": 0, "Wild": 0}
total_score = 0

def print_scores(score_list):
    for item in score_list:
        print(item + ": " + str(score_list[item]))

def score(rolls, field):
    global scores
    points = sum(rolls)
    assert scores[field] == 0
    scores[field] = points

def field_strip(fields):
    hold = []
    for x in fields:
        if scores[x] == 0:
            hold.append(x)
    return hold
    
def turn():
    rolls = roll_dice()
    rolls = reroll(rolls)
    rolls = reroll(rolls)
    print(*rolls, sep=", ")
    valid_sets = sets_counter(dice_counter(rolls))
    valid_sets = field_strip(valid_sets)
    if len(valid_sets) == 0:
        print("You can not score. Your ship has sunk.")
        return False
    else:
        print("\nYour score this round: "+str(sum(rolls))+".")
        for i, x in enumerate(valid_sets,1):
            print(str(i)+": "+x)
        choice = int(input("Choose a field: "))
        score(rolls, valid_sets[choice-1])
        return True

print("""Sinking Ship: Each turn, you will roll 6 dice.
You may then pick some to keep and reroll the rest twice. 
Then, you must pick a score field to use.
Each field can only be used once, so plan wisely.
The game ends if you can't score on any turn.
Get the highest score you can.
""")
looping = True
while looping:
    print_scores(scores)
    total_score = sum(scores.values())
    print("Total: " + str(total_score)+"\n")
    looping = turn()
    print("")
    if min(scores.values()) != 0:
        print("Every field is full. Your ship has sunk.")
        break
print_scores(scores)
total_score = sum(scores.values())
print("\nFinal Score: "+str(total_score))
if total_score >= 300:
    print("Rank A! Well played!")
elif total_score >= 275:
    print("Rank B. Good game.")
elif total_score >= 250:
    print("Rank C.")
elif total_score >= 225:
    print("Rank D. Better luck next time.")
else:
    print("Rank F. Better luck next time.")
