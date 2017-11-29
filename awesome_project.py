#!/usr/bin/env python

def count(target):
    for i in range(1, target + 1):
        print(str(i))

if __name__ == "__main__":
    print("I now count from 1 to target, inclusive!")
    count(10)
