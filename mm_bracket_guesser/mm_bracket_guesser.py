#!/usr/bin/env python

import argparse
import random


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-1', dest='team_1',
                        required=True, help='Team 1 rank')
    parser.add_argument('-2', dest='team_2',
                        required=True, help='Team 2 rank')
    return parser.parse_args()


def choose_loser(team_1, team_2):
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


def pick_em():
    args = parse_args()

    winner, loser = choose_loser(args.team_1, args.team_2)
    print 'Winner is {0}, loser is {1}'.format(winner, loser)


if __name__ == '__main__':
    pick_em()
