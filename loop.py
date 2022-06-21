#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on June 2022
# This program displays every integer from 1000-2000


def main():
    # This Is The Main Function

    print("This program displays every integer from 1000 to 2000.")

    loop_counter = 0

    # Output
    for loop_counter in range(1000, 2000 + 1):
        if loop_counter % 5 == 4:
            print("{0}  ".format(loop_counter))
        else:
            print("{0}  ".format(loop_counter), end="")


if __name__ == "__main__":
    main()
