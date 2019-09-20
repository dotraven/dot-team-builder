import argparse
import math
import random

parser = argparse.ArgumentParser()
parser.add_argument("--teamsize", type=int,
                    help="max team size - integer non negative preferably")
parser.add_argument("--playerslist", type=str, nargs='+',
                    help="space delimited list of players to be divided in to teams")
args = parser.parse_args()

players = args.playerslist
teamsize = args.teamsize

if players is None or teamsize is None:
    print("Too few valid arguments")
    exit(1)
if teamsize <= 0:
    print("Invalid team size")
    exit(1)
try:
    random.shuffle(players)
    loop_count = math.ceil(len(players) / teamsize)
    print("\nGenerating teams with team size of {}\n".format(teamsize))
    for team_number in range(loop_count):
        print("Team {}:".format(team_number))
        print(*players[team_number * teamsize:(team_number + 1) * teamsize], sep=', ')
        print("")
except Exception as error:
    print("Exception occurred - {}", error)
    exit(2)
