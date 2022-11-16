#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Nov. 15, 2022
# This program prints all possible
# RGB codes


def main():
    # introductory paragraph
    print("This program prints all possible")
    print("RGB codes")
    print("")

    # initializing red
    red = 0;

    # initializing green
    green = 0;

    # initializing blue
    blue = 0;

    start = input("Enter Y to start program: ")

    # starting do while loop
    while start == "Y":
        # blue loop
        if blue < 255:
            # printing colours
            print("{} {} {}".format(red, green, blue))
            blue = blue + 1
        # green loop
        elif green < 255:
            if blue == 255:
                blue = 0
                green = green + 1
            # printing colours
            print("{} {} {}".format(red, green, blue))
        # red loop
        elif red < 255:
            if green == 255:
                green = 0
                red = red + 1
            # printing colours
            print("{} {} {}".format(red, green, blue))
        else:
            # printing colours
            print("{} {} {}".format(red, green, blue))
            print("This is the end.")
            # breaking loop
            break


if __name__ == "__main__":
    main()
