#!/usr/bin/env python

import random


def choose_winner_loser(team_1, team_2):
    # get shuffled team picks list, weighted by team rank
    picks = []
    for i in range(int(team_1)):
        picks.append(team_1)
    for i in range(int(team_2)):
        picks.append(team_2)
    random.shuffle(picks)

    # pick winner randomly from team picks list
    index = random.randint(0, len(picks)-1)
    loser = picks[index]
    winner = team_1 if loser == team_2 else team_2
    return winner, loser


def get_starting_bracket():
    bracket = []
    sub_bracket = [(1, 16), (8, 9), (5, 12), (4, 13), (6, 11), (3, 14), (7, 10),
                   (2, 15)]
    for i in range(4):
        bracket.append(sub_bracket)
    return bracket


def group(lst, n):
    for i in range(0, len(lst), n):
        val = lst[i:i+n]
        if len(val) == n:
            yield tuple(val)


def solve_sub_bracket(bracket):
    winners = []
    print bracket
    for i in bracket:
        winner, loser = choose_winner_loser(i[0], i[1])
        winners.append(winner)

    if len(winners) == 1:
        print winners
    else:
        next_bracket = list(group(winners, 2))
        if len(next_bracket) > 0:
            return solve_sub_bracket(next_bracket)
    return


def solve_bracket(main_bracket):
    for bracket in main_bracket:
        solve_sub_bracket(bracket)


def pick_em():
    starting_bracket = get_starting_bracket()
    solve_bracket(starting_bracket)


if __name__ == '__main__':
    pick_em()
