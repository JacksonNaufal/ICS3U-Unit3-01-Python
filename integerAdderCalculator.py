#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a basic integer adder calculator


def main():
    # This is a calculator that calculates your first number plus your second number

    # input
    int1 = int(input("Enter your first number here (Integer): "))
    int2 = int(input("Enter your second number here (Integer): "))

    # process
    answer = int1 + int2

    # output
    print("\nThe total of both of your integers is {0}.".format(answer))
    print('\n{0} + {1} = {2}'.format(int1, int2, answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
