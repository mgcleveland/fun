#!/usr/bin/env python
import random


WEIGHTS = {"1": [5, 6],
           "2": [4, 5],
           "3": [3, 4],
           "4": [2, 3],
           "5": [1, 2]}


def get_team_ranges(team_1, team_2, depth):
    favorable_weight = WEIGHTS[str(depth)][0]
    unfavorable_weight = WEIGHTS[str(depth)][1]

    # 1st place never loses in the first round ever
    if (int(team_1) == 1 or int(team_2) == 1) and (depth == 1):
        team_1_range = int(team_1)
        team_2_range = int(team_2)
    elif int(team_1) < int(team_2):
        team_1_range = int(team_1) * unfavorable_weight
        team_2_range = int(team_2) * favorable_weight
    else:
        team_1_range = int(team_1) * favorable_weight
        team_2_range = int(team_2) * unfavorable_weight
    return team_1_range, team_2_range


def choose_winner_loser(team_1, team_2, depth):
    # get shuffled team picks list, weighted by team rank
    picks = []
    team_1_range, team_2_range = get_team_ranges(team_1, team_2, depth)

    for i in range(team_1_range):
        picks.append(team_1)
    for i in range(team_2_range):
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


def solve_sub_bracket(bracket, depth):
    winners = []
    print bracket
    for i in bracket:
        winner, loser = choose_winner_loser(i[0], i[1], depth)
        winners.append(winner)

    if len(winners) == 1:
        print winners
    else:
        next_bracket = list(group(winners, 2))
        if len(next_bracket) > 0:
            return solve_sub_bracket(next_bracket, (depth+1))
    return


def solve_bracket(main_bracket, depth):
    for bracket in main_bracket:
        solve_sub_bracket(bracket, depth)


def pick_em():
    starting_bracket = get_starting_bracket()
    solve_bracket(starting_bracket, 1)


if __name__ == '__main__':
    pick_em()
