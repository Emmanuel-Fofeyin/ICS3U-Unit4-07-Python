#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Nov 2022
# This program shows every number from 1000 to 2000


def main():

    # Process and Output
    for counter in range(1000, 2001):
        if counter % 5 == 0:
            print("")
            print(counter, end=" ")
        else:
            print("{0} ".format(counter), end="")

    print("\nDone.")

if __name__ == "__main__":
    main()