# Program name: Ten numbers
# Program Purpose: Getting 10 numbers from the user and displaying in various sorted order.
# Program Author: Edward Nigma
# Date completed: 11/5/24

# Declare variables
numbers = []

# Program Introduction
print('Welcome to me program')

for num in range(1, 11):
    number = input(f'please enter number {num}: ').strip()
    number = int(number)
    numbers.append(number)

# output the results
print('THIS IS WRONG - DO NOT DO THIS ON A TEST')
print(numbers)

print('Here are the numbers:')
for value in numbers:
    print(value, end= ' ')

print('\nHere are the values in numerical order:')
numbers.sort()

for value in numbers:
    print(value, end=' ')

print('\nHere are the values in reverse numerical order: ')
numbers.reverse()

for value in numbers:
    print(value, end=' ')

# Thank the user
print('\nThanks for using my program')