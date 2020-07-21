# Ukufu Tech Task

A coding exercise given as an interview.

## The Task

Please develop your code on the language of your choice taking into
consideration that this would be a production level code.
A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau,
which is curiously rectangular, must be navigated by the rovers so that their on-board
cameras can get a complete view of the surrounding terrain to send back to Earth.
A rover’s position and location is represented by a combination of x and y coordinates and
a letter representing one of the four cardinal compass points. The plateau is divided up
into a grid to simplify navigation. An example position might be 0, 0, N, which means the
rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are
‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ make the rover spin 90 degrees left or right respectively, without
moving from its current spot. ‘M’ means move forward one grid point, and maintain the
same heading.

Assume that the square directly North from (x, y) is (x, y+1).

## Input
The first line of input is the upper-right coordinates of the plateau, the lower-left
coordinates are assumed to be 0,0.

The rest of the input is information pertaining to the rovers that have been deployed. Each
rover has two lines of input. The first line gives the rover’s position, and the second line is a
series of instructions telling the rover how to explore the plateau.
The position is made up of two integers and a letter separated by spaces, corresponding to
the x and y coordinates and the rover’s orientation.
Each rover will be finished sequentially, which means that the second rover won’t start to
move until the first one has finished moving.
Output:
The output for each rover should be its final coordinates and heading.

### Example Input
5 5

1 2 N

LMLMLMLMM

3 3 E

MMRMMRMRRM

### Expected Output
1 3 N

5 1 E

## Usage

To run main program
```bash
python main.py
```
1. You will be asked to enter in the upper right-hand coordinate of the grid (with the lower left-hand being at "0 0." Enter in the format "X Y", including the space in the middle.

2. You will then enter the coordinates of the first rover along with the cardinal direction it is facing, in the format "X Y Direction." Acceptable directions are "N" for north, "S" for south, "E" for east, and "W" for west. This is case insensitive.

3. You then enter the directions as a continuous string that consists solely of "M" to move forward 1 space, "L" to rotate the rover's direction 90 degrees counter-clockwise, and "R" to rotate the rover's direction 90 degrees clockwise.

4. You will then be asked if you wish to continue adding rovers. Entering 0 will stop adding rovers, and anything else will add another rover, repeating steps 2 - 4.

5. Once a 0 is entered, the program will execute each of rover's moves, 1 at a time until completion*.

*A rover's moves are considered complete when:

a. A rover has completed all instructions given.

b. A rover's next move will cause it to fall off the grid, and must abort 
future instructions to avoid damage.

c. A rover's next move will cause it to occupy the space of another rover, 
and must abort further instruction to avoid a crash.

## Files

### main.py
The file that contains main() which runs the entire program to completion, and prints the results.

### area.py
The functions that deal with creating the initial internal state of the plateau that the rovers drive on. Creates a rectangular grid, knowing that the lower left corner is designated as "0 0", and the upper right corner is given by the user.
#### functions
upper_edge (no args) - takes in the user input about the upper boundaries of the grid, and makes sure the user entries are correctly formatted.
Returns - coordinates of the upper edge in a tuple (X,Y)

create_grid (no args)- uses dimensions given from upper_edge to return a numpy grid of ''.
Returns - a numpy array of '' with dimensions of (X+1,Y+1) to account for the 0 index.

### rover.py
The file that deals with creating a rover class, as well as populating the grid with them.
#### classes
Rover(x, y, direction, instructions, grid) - Abstraction for our Rovers. It is initialized with
x - its x coordinate on the grid
y - its y coordinate on the grid
direction - its cardinal direction the rover is facing (N, S, E, W)
instructions - the string of instructions the Rover will execute. Made up of 'L', 'R', and 'M' moves.
grid - the grid it is moving on
##### class methods
make_move - executes the next instruction on the rover's instructions, and updates the grid accordingly.
final_placement - returns the coordinate placement of the rover on the grid

#### functions
populate (g) - The function that takes in g, the grid that the rovers sit on, and gets user input of the X and Y coordinates, and direction rovers are facing. It then takes in a sequence of moves, and loops through taking in more and more rovers until the user enters 0 to designate they are finished adding rovers.
Returns - a list of Rover objects

### utils.py
Utility functions used by other parts of the program.
#### functions
check_letters (l) - takes in l, a string a letters, and determines if it is made up purely of 'L', 'M', and 'R' characters, case insensitive.
Returns - True if it is exclusively those characters, False otherwise.


### tests.py
Unit and stress tests

#### functions
fifty_fifty (one, two) - a test specific function that takes in 2 inputs, one and two, and returns one of them at random.
Return one or two (random)

#### classes
TestStringMethods - the unit test class that runs each of the following tests.

##### class methods
test_utils - tests functions in utils.py (currently only check_letters).
test_area - tests functions in area.py to create grids for the rovers to navigate.
test_rover_run - comprehensive step by step of a single rover run across a grid.
test_stress_rover - tests the program with 9998 rovers moving in series.
test_crash_and_fall - test to make sure rovers don't crash into each other or fall off the grid.

### errors.py
Custom errors that are used in other parts of the program that are project specific
#### classes
Error - Base class for other exceptions

ValueTooSmallError - Raised when the input value is too small

ValueTooLargeError - Raised when the input value is too large

AlphaError - Raised when the input value is not a letter

OffGridError - Raised when the rover will fall off the grid

CrashError - Raised when the rover will crash into another rover
