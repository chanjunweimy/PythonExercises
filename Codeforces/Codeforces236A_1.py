# Author: Chan Jun Wei
# Website: Codeforces
# Problem: 236 A: Boy or Girl

def printIsBoyOrGirl(name):
    CHAR_NUM = 26
    alphaberts = [0] * CHAR_NUM

    for charName in name:
        index = ord(charName) - ord('a')
        if index < 0 or index >= CHAR_NUM:
            #got non lower case alphabert character
            return
        alphaberts[index] += 1

    numDistinct = 0    
    for i in range(CHAR_NUM):
        if alphaberts[i] > 0:
            numDistinct += 1

    if numDistinct % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

name = input()
printIsBoyOrGirl(name)
