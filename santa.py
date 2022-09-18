# Inspiration taken from https://github.com/kilgallin/SecretSanta2
import random

# Take names as input
print('Enter names, seperated by commas.')
input = input()
input = input.replace(' ', '')
names = input.split(',')

# Parallel ist to store partners
partners = list()

validFlag = False # Control if randomly generated partner is valid
random.seed()

# Assign random partners
for name in names:
    while not validFlag:
        candidate = random.choice(names)
        if (candidate != name) and candidate not in partners: # Dont reuse partners, dont assignment people themselves
            validFlag = True
            partners.append(candidate)
    validFlag = False

# Print results
print('------------------------------')
for i, name in enumerate(names):
    print(name + ' buys a gift for ' + partners[i] + '.')
print('------------------------------\nHave a merry Christmas!')
