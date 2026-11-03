#!/usr/bin/env python3
for first in range(9):
    for second in range(first + 1, 10):
        print("{}{}".format(first, second),
              end="\n" if first == 8 and second == 9 else ", ")
