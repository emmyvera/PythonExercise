# Handling files with python
# Using python to write note to a file
# file = open('filename.txt', 'w') Open and create
# file.write('Line 1')
# file.close() to effect the changes
# using loop the write to a file
# r, r+, w, w+, a, a+
# with method for opening file
# with open(name, method) as file:

# file = open('newfile.txt', 'r')
# content = file.read()
# file.close()

# print(content)

# a = ['Cat', 'Dog', 'Sheep', 'Wolf']
# file = open('Animal.txt', 'a')
# for i in a:
#     file.write(i+'\n')
# file.close()

username = input('Your Name ')
userage = input('Your age ')
userW = input('Your Weight ')
userH = input('Your Height ')

bmi = float(userW) / (float(userH))**2

sent = ''
if bmi >= 25:
    sent='Overweight'
elif bmi >= 18:
    sent='Normal'
else:
    sent='Underweight'

stars = '*'*20
result = f"""
{stars}
Name: {username}
Age: {userage}
Height: {userH}m
Weight: {userW}Kg
{stars}
Your Result
BMI (Body Mass Index): {bmi}
BMI Status: {sent}
Thanks
{stars}  
"""

with open('result.txt', 'a') as file:
    file.write(result)    