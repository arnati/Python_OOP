import sys


class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __bool__(self):
        return True if self.score > 0 else False


# lst_in = [
#     'Балакирев; 34; 2048',
#     'Mediel; 27; 0',
#     'Влад; 18; 9012',
#     'Nina P; 33; 0'
# ]
lst_in = list(map(str.strip, sys.stdin.readlines()))

players = [Player(*row.split("; ")) for row in lst_in]
players_filtered = [*filter(bool, players)]
