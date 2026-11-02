#!/usr/bin/env python3
alphabet = ""
for code in range(97, 123):
    letter = chr(code)
    if letter != "e" and letter != "q":
        alphabet += letter
print(alphabet)
