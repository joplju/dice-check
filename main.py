import random
from itertools import chain
from collections import Counter, OrderedDict

num_trials = 1000000

print(f'Testing each scenario {num_trials} times')

class OrderedCounter(Counter, OrderedDict):
    pass


def roll_dice(num_dice, num_faces, reroll_ones=False):
    results = []
    i = 0
    while i < num_dice:
        thisResult = random.randint(1, num_faces)
        if reroll_ones:
            while thisResult == 1:
                thisResult = random.randint(1, num_faces)
        results.append(thisResult)
        i += 1
    return results

def drop_lowest(dice_rolls, num_to_drop):
    dice_rolls.sort()
    return dice_rolls[num_to_drop:]

def count_and_print(dice_rolls):
    dice_rolls.sort()
    dice_counts = Counter(dice_rolls)
    for result, count in dice_counts.items():
        pct = count / dice_counts.total() * 100
        print(f'Number of {result}s: {count} - ({pct:.2f}%)')

def roll_and_drop(num_dice, num_faces, num_dropped, reroll_ones=False):
    dice_rolls = roll_dice(num_dice, num_faces, reroll_ones=reroll_ones)
    return drop_lowest(dice_rolls, num_dropped)

# Roll 4d6, drop 1; do this six times
print('### 4d6, drop 1 for each stat ###')
all_dice = []
for i in range(num_trials):
    single_char = [roll_and_drop(4, 6, 1) for i in range(6)]
    single_char = list(chain(*single_char))
    all_dice.append(single_char)
all_dice = list(chain(*all_dice))
assert len(all_dice) == 18*num_trials
count_and_print(all_dice)

# Roll 20d6, drop 2; combine any way
print('### 20d6, drop 2; combine any way ###')
all_dice = []
for i in range(num_trials):
    all_dice.append(roll_and_drop(20, 6, 2))
all_dice = list(chain(*all_dice))
assert len(all_dice) == 18*num_trials
count_and_print(all_dice)

# Roll 25d6, rerolling 1s; drop lowest 7; combine any way
print('### 25d6, drop 7, reroll 1s; combine any way ###')
all_dice = []
for i in range(num_trials):
    all_dice.append(roll_and_drop(25, 6, 7, reroll_ones=True))
all_dice = list(chain(*all_dice))
assert len(all_dice) == 18*num_trials
count_and_print(all_dice)
