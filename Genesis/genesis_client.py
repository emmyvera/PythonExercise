import genesis_database as gdb
from os.path import exists

file_exists = exists('genesis.db')

print('Welcome to Genesis Restourant')
print('What is your name?')
name = input()
print(f'Can I take your orders? {name.title()}')
print('We have pizza; Enter (L) for Large - 2000, (M) Medium - 1500, (S) Small - 1200')
pizza = input()
print('Should I add Pepperoni, 200 for Small Size and 300 for Large Size')
print('Enter Y for Yes and N for No')
pepperoni = input()
print('Should I add Extra Cheese, 100 for all size')
print('Enter Y for Yes and N for No')
cheese = input()

bill = 0

# # Selection of Pizza
if pizza == 'S':
    bill = bill + 1200
elif pizza == 'M':
    bill = bill + 1500
elif pizza == 'L':
    bill = bill + 2000


# Selection of Pepperoni
if pepperoni == 'Y':
    if pizza == 'S':
        bill = bill + 200
    else:
        bill = bill + 300

# Selection of Extra Cheese
if cheese == 'Y':
    bill = bill + 100

if file_exists:
    pass
else:
    gdb.create_table()

gdb.insert(name=name, pizza=pizza, pepperoni=pepperoni, chesse=cheese, price=bill)

print(f'Your total bill is {bill}')
print(f'Thanks for choosing us! Do come again next time!!')