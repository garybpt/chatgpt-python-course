import random



number_of_streaks = 0

for experiment_number in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    while experiment_number < 100:
        if random.randint(0, 1) == 0:

    # Code that checks if there is a streak of 6 heads or tails in a row.


print('Chance of streak: %s%%' % (number_of_streaks / 100))