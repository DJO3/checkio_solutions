"""
Nicola has built a semi-automatized painting system, but this system can paint only one side of an item. After that, an operator must reload the machine and paint the other side (the system detects painted sides automatically). The painting process always takes the same amount of time. The camera can paint K surfaces at a time. Nicola wants Stephan to operate the painting machine and he needs to develop an algorithm for Stephan which will allow him to paint N (0 < N ≤ 10) surfaces in the shortest possible timeframe. Be careful that you don't paint the item more than two times.
system
The items are numbered from 0 to 9. You are given the paint holding capacity of the machine (K) and the quantity of items (N). You should return the sequence Stephen must paint as a string, where each action is the numbers of painted items. Actions separated by comma (",").
Input: Capacity of the painting system and quantity of items as integers.
Output: The sequence of actions as a string.
Precondition:
0 < capacity ≤ 10
0 < number ≤ 10
"""

def checkio(capacity, number):
    # Converts "123" into "112233"
    doubled = "".join(str(x) for x in range(number)) * 2
    
    # Chooses split point to add comma
    split = number if capacity > number else capacity
    pattern = str()
    chunk = str()
    
    for side in doubled:
        if len(chunk) == split:
            pattern = pattern + chunk + ','
            chunk = str() + side 
        else:
            chunk = chunk + side
    
    if chunk:
        pattern = pattern + chunk
    
    return pattern

