# Task 1: Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number less than the asked number.
x= int(input('enter a number:'))
y=list()
for m in range(2,x//2+1):
    if x%m==0:
        y.append(m)
print (y)

# Task 2:  Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.
x= int(input('enter a number:'))
y= int(input('enter a number:'))
for m in range(2, x//2):
    if y**m == x:
        print(f'{y}**{m}={x}')
        break
    else:
        print('there is no operation')
        break
#  Task 3: Write a Python program that counts and displays the vowels of a given string ignoring the letter case.
v = 'aeiou'
count = 0
s= input('enter a string:')
for v in v:
    if v in s.lower():
        count += s.count(v)
print(f'number of vowels is : {count}')

# Task 8: Write a Python script that displays the following pattern from 1 to n where n is entered by the user.
#
# If the user enters 6 it will display:
#
# 1
#
# 22
#
# 333
#
# 4444
#
# 55555
#
# 666666
x= int(input('enter a number:'))
for n in range (x+1):
    print(str(n)*n)

# Task 9: Write a Python program that finds the common characters that appear in two given strings.
s1= 'i sleep'
s2= 'i read'
cc=''
for n in s1:
    if n in s2:
        if n not in cc:
            cc+=n
print(cc)

# Task 10:  Write a Python program that iterates over the integers from 1 to 50.
# For multiples of three print "Foo" instead of the number and for multiples of five print "Bar".
# For numbers that are multiples of both three and five print "FooBar".
for x in range(51):
    if x%3==0:
        print('Foo')
        continue
    elif x%5==0:
        print('Bar')
        continue
    elif x%3==0 and x%5==0:
        print('FooBar')
print(x)

# Task 11: Write a Python script that prints out the Fibonacci series up to a given number n.
# Example: if n is 23 it will print out 0, 1, 1, 2, 3, 5, 8, 13, 21
x = 54
a,b=0,1
while a<=x:
    print(a,'', end='')
    a,b= b, a+b

# Task 12: Write a Python script that draws the following pattern using for loops.
#
# *
#
# * *
#
# * * *
#
# * * * *
#
# * * * * *
#
# * * * *
#
# * * *
#
# * *
#
# *
n=5
for x in range(n):
    for x1 in range (x):
        print('*', end='')
    print('')
for x in range(n,0,-1):
    for x1 in range(x):
        print('*',end='')
    print('')

# Task 12: (alternative)
#
x='*'
for n in range(5):
    print(x*n)
for n in range(5,0,-1):
    print(x*n)




