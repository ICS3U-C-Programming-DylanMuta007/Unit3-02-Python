#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : March 2025
# This program makes the use guess randomly generated number 1 - 10
import constants


def main():
    # asks the user to guess a number between 1 and 10
    user_guess = int(input("Guess a number between 1 and 10 : "))

    if (
        user_guess == constants.NUMBER
    ):  # if the users guess = the random generated number it print good job
        print("good job guessing correctly :)\n")
    if (
        user_guess != constants.NUMBER
    ):  # if # if the users guess does not = the random generated number it print got ir wrong
        print("got it wrong :(")
        print("the right number was", constants.NUMBER)  # shows correct number


if __name__ == "__main__":
    main()  # runs the program
