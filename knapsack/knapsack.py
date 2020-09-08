#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    # print("items ----->", items)
    # print("capacity ----->", capacity)

    # # steps
    # # Create a loop that looks over all of the items and creates a ratio score for them.
    # # Return all of the items with a ratio score to a new array
    # ratioList = [{"index": treasure[0], "size": treasure[1], "value": treasure[2], "ratio": treasure[2] - treasure[1]}
    #              for treasure in items]
    # print("list -->", ratioList)

    # bestItem = {'value': 0, 'chosen': []}
    # currentBest = ratioList[0]
    # print("xx", currentBest)

    # while capacity <
    #     for item in ratioList:
    #         if item['ratio'] > currentBest['ratio']:
    #             currentBest = item

    # Compare the ratios and grab the items with the highest score.
    # Use a while loop to grab items until the cap runs out


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
