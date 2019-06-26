import sys
import math
from collections import deque

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cards_p1 = deque()
#cards_p1 = deque(["10D", "9S", "8D", "KH", "7D", "5H", "6S"])
#cards_p1 = deque(["AD", "KC", "QC"])
cards_p2 = deque()
#cards_p2 = deque(["10H", "7H", "5C", "QC", "2C", "4H", "6D"])
#cards_p2 = deque(["KH", "QS", "JC"])
stakes_p1 = deque()
stakes_p2 = deque()

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    cards_p1.append(cardp_1)

m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    cards_p2.append(cardp_2)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# 1. top card 보기
# - 드로우 못하면 무승부
# - 1p 카드 stakes_p1로, 2p 카드 stakes_p2로
#
# 2. fight
# - 승패 비교로직
# - war
#   . 3장씩 stakes로(드로우 못하면 무승부)
#   . 1장 드로우 and fight(드로우 못하면 무승부)
#
# 3. 정리
# - stakes_p1 넣기 then stakes_p2 넣기
#
# 4. check_win

values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
turn_count = 0
is_pat = False

P1_WIN = 101
P2_WIN = 102
DRAW = 103

def draw_cards(n):
    counter = n
    while counter > 0:
        card_p1 = cards_p1.popleft()
        stakes_p1.append(card_p1)
        card_p2 = cards_p2.popleft()
        stakes_p2.append(card_p2)
        counter = counter - 1


def fight():
    card1 = stakes_p1[-1]
    card2 = stakes_p2[-1]
    card1_v = values[card1[:-1]]
    card2_v = values[card2[:-1]]

    if card1_v > card2_v:
        result = P1_WIN
    elif card1_v == card2_v:
        result = DRAW
    else:
        result = P2_WIN

    return result


def check_winner():
    if len(cards_p1) == 0:
        winner = 2
    elif len(cards_p2) == 0:
        winner = 1
    else:
        winner = 0

    return winner


def put_back_cards(player):
    if player == 1:
        deck = cards_p1
    else:
        deck = cards_p2

    while len(stakes_p1) > 0:
        card = stakes_p1.popleft()
        deck.append(card)

    while len(stakes_p2) > 0:
        card = stakes_p2.popleft()
        deck.append(card)


while check_winner() == 0:
    turn_count = turn_count + 1
    try:
        draw_cards(1)
        while fight() == DRAW:
            draw_cards(4)
    except IndexError:
        is_pat = True
        break

    if fight() == P1_WIN:
        put_back_cards(1)
    else:
        put_back_cards(2)

winner = check_winner()
if is_pat:
    print("PAT")
else:
    print('{0} {1}'.format(winner, turn_count))
