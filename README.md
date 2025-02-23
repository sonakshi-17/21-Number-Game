# 21-Number-Game
Certainly! Below is a detailed description of the provided code, which implements a simple number game where a player competes against a computer. The goal is to avoid reaching the number 21, and the player must input consecutive integers during their turn.

Code Breakdown
1. Function Definitions
check_consecutive(lst)

Purpose: This function checks if the numbers in the list lst are consecutive integers.
Parameters:
lst: A list of integers.
Returns:
True if all numbers in the list are consecutive; otherwise, False.
Logic: It iterates through the list and checks if the difference between each number and the previous one is exactly 1.
nearest_multiple(n)

Purpose: This function calculates the nearest multiple of 4 that is greater than the given number n.
Parameters:
n: An integer.
Returns:
The next multiple of 4 greater than n.
Logic: It uses integer division to find the next multiple of 4.
lose()

Purpose: This function is called when the player loses the game.
Logic: It prints a losing message and exits the program.
2. Main Game Logic
play_game()

Purpose: This function contains the main game loop and handles the game logic.
Variables:
xyz: A list to store the numbers played by both the player and the computer.
last: An integer to keep track of the last number played.
Game Loop:

The game runs indefinitely until the player loses or wins.
The player is prompted to choose between taking the first chance (F) or the second chance (S).
First Chance (F):

If the player chooses F, they enter how many numbers they want to input (1 to 3).
The player inputs their numbers, which are added to the xyz list.
The game checks if the numbers are consecutive using check_consecutive().
If the player inputs valid consecutive numbers, the computer automatically adds the next consecutive numbers to the list.
If the last number played is 21, the player loses.
Second Chance (S):

If the player chooses S, the computer starts by adding one number (1).
The player then inputs their numbers, which are also checked for consecutiveness.
The computer calculates how many numbers it can add based on the nearest multiple of 4.
The game continues until the player reaches or exceeds 21.
3. Input Handling
The game uses input() to get user input and int() to convert it to an integer.
It includes error handling using try-except blocks to catch non-integer inputs and invalid ranges.
4. Winning and Losing Conditions
The player loses if:
They input non-consecutive integers.
They reach the number 21.
The game continues until one of these conditions is met.
5. Program Entry Point
The if __name__ == "__main__": block ensures that play_game() is called when the script is executed directly.
Summary
The code implements a simple turn-based game where the player and the computer take turns inputting consecutive integers. The player must avoid reaching the number 21, and the game checks for valid inputs and consecutive sequences. The game ends when the player loses, and a message is displayed. The structure of the code is straightforward, with clear separation of concerns through functions, making it easy to understand and modify.
