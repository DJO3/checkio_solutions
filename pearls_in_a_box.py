"""
While Stephen is running cargo, Nicola and Sophia invented a game using the boxes.

To start the game, they put several black and white pearls in one of the boxes.
Each robots have Nth moves, then initial set are restored for a next player.
For each move, the robot take a pearl out of the box and put one of the opposite color back.
The winner is the one who pulls the white pearl on the Nth step (or +1 point if they play many parties).

Our robots don't like indeterminacy and want to know the probability of a white pearl on the Nth step.
The probability is a value between 0 (0% chance or will not happen) and 1 (100% chance or will happen).
The result is a float from 0 to 1 with two digits precision (±0.01).

You are given a start set of pearls as a string that contains "b" (black) and
"w" (white) and the number of the step (N). The order of the pearls does not matter.
probability

Input: The start sequence of the pearls as a string and the step number as an integer.

Output: The probability for a white pearl as a float.

Example:
checkio('bbw', 3) == 0.48
checkio('wwb', 3) == 0.52
checkio('www', 3) == 0.56
checkio('bbbb', 1) == 0
checkio('wwbb', 4) == 0.5
checkio('bwbwbwb', 5) == 0.48

How it is used: This task introduces you to the basics of probability theory and statistics.
Fun fact: regardless of the initial state, as the number of steps increases, the probability approaches 0.5!

Precondition: 0 < N ≤ 20
0 < |pearls| ≤ 20
"""


def checkio(pearls, step):
    total_pearls = len(pearls)
    white_pearls = pearls.count('w')
    even = 1 - ((2 * white_pearls) / total_pearls)
    odd = (1 - (2 / total_pearls))**(step - 1)

    result = 1 / 2 * (1 - even * odd)
    return round(result, 2)

print(checkio('wwb', 3))
