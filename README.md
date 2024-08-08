# Euclidean Distance Calculator
- This Python script calculates the Euclidean distance between two randomly selected points in a 2D space.
- The points are selected from a list of all possible pairs of integer coordinates within the range defined by the user’s input.

##  How It Works
### User Input Validation:
- The script first prompts the user to input an integer value.
- The input is validated to ensure it is an integer. The script checks and handles cases where the input might be a boolean, float, or string, giving appropriate feedback until a valid integer is provided.

### Generating Coordinate Pairs:
- A list (depo) is created, containing all possible (x, y) coordinate pairs within the range [0, user_input] for both x and y.

### Randomizing the List:
- The list of coordinate pairs is shuffled randomly to ensure that the pairs are in a random order.

### Selecting Points:
- Two consecutive points, A and B, are selected from the shuffled list based on the user’s input value. Specifically, the n-th and (n+1)-th pairs are selected, where n is the integer provided by the user.

### Calculating Euclidean Distance:
- The Euclidean distance between points A and B is calculated using the Euclidean distance formula. 
- The calculated distance is then printed to the console.

#### Example Output
If the user inputs the number 2, the script will:
- Create a list of coordinate pairs for all x and y values from 0 to 2 (inclusive).
- Randomly shuffle this list.
- Select the 2nd and 3rd pairs from the shuffled list.
- Calculate and print the Euclidean distance between these two points.

##### Prerequisites
- Python 3.x
- random and math modules (both are part of the Python Standard Library)

##### How to Run the Script
1. Ensure Python 3.x is installed on your machine.
2. Copy the code into a Python file (e.g., euclidean_distance.py).
3. Run.

![GIF Description](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbm5weDZxc3d1NmxndmUzODE4OGNnMjU5MWFnZG43aHhodWpraTk1MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0K42fEl2ldQOrNba/giphy.gif)

### Additional Notes
- The script includes comprehensive error handling for user input, ensuring that only valid integers are accepted.
- The Euclidean distance calculated is the straight-line distance between the two selected points in the 2D plane.
