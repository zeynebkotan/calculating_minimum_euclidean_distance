import random
import math

while True:
    user_input = input("Please give a number: ")
    try:
        user_input = int(user_input)  # Converting the string to integer
        break  # If conversion is successful, exit the loop
    except ValueError:  # Handling with ValueErrors
        # Checking for boolean input
        if user_input.lower() in ["true", "false"]:
            print("You wrote a boolean, please give an integer.")
        # Checking for float input
        elif user_input.replace('.', '', 1).isdigit() and '.' in user_input:
            print("You wrote a float, please give an integer.")
        # Checking for string input (anything containing letters)
        elif any(char.isalpha() for char in user_input):
            print("You wrote a string, please give an integer.")
        else:
            print("Invalid input, please give an integer.")

# Creating a list with (x, y) pairs
depo = []
for x in range(user_input + 1):
    for y in range(user_input + 1):
        depo.append((x, y))

# Shuffling the list to get a random order
random.shuffle(depo)

# Selecting the n th and (n+1) th pairs based on user_input
n = user_input
A = depo[n]
B = depo[n + 1]

# Printing the results to clearly see which points we have:
print("Depo list:", depo)
print("A:", A)
print("B:", B)

x1, y1 = A
x2, y2 = B


def euclidean_distance(x1, x2, y1, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("The distance between point A and B is " + str(distance) + " and it's calculated by euclid's equation.")


euclidean_distance(x1, x2, y1, y2)
