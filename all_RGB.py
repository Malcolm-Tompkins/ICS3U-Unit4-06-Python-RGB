#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 24, 2021
# Determines all values of RGB

import constants


def main():
    loop_counter1 = 0
    loop_counter2 = 0
    loop_counter3 = 0
    for loop_counter1 in range(constants.byte):
        loop_counter1 = loop_counter1 + 1
        for loop_counter2 in range(constants.byte):
            loop_counter2 = loop_counter2 + 1
            for loop_counter3 in range(constants.byte):
                loop_counter3 = loop_counter3 + 1
                print("RGB({0},{1},{2})".format(loop_counter1,
                                                loop_counter2, loop_counter3))


if __name__ == "__main__":
    main()
