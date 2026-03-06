# Task 1: Digital Root Sequence
steps = 0
value = int(input("Please enter a positive integer greater than 9: "))

while value > 9:
    # end="" prevents print() from automatically dropping to a new line
    print(value, end="")
    newVal = 0

    while value > 0:
        newVal += value % 10
        value //= 10  # // is used for integer division in Python

    value = newVal
    steps += 1
    print("-->", end="")

print(value)
print("Final Value :", value)
print("Total steps :", steps)
print()
# Task 2: FizzBuzz


fizz = 0
buzz = 0
fizzBuzz = 0

print("Please enter a number between 10 and 100:")
value2 = int(input())

while value2 < 10 or value2 > 101:
    value2 = int(input("Invalid input. Please enter a number between 10 and 100: "))

for i in range(1, value2 + 1):
    if i % 7 == 0:
        print(f"({i} is skipped)")
        continue

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzBuzz += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz += 1
    else:
        print(i)

print("--Summary--")
print(f"Fizz count : {fizz}\nBuzz count : {buzz}\nFizzBuzz count : {fizzBuzz}")
print()

#Task 3

print("Please enter a number between 3 and 9:")
count = int(input())

while count < 3 or count > 9:
    count = int(input("Invalid input. Please enter a number between 3 and 9: "))

for i in range(count):
    for j in range(i + 1):
        print(j + 1, end="")
    print()

for i in range(count - 1, 0, -1):
    for j in range(i):
        print(j + 1, end="")
    print()