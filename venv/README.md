
```bash
usage: team-builder.py [-h] [--teamsize TEAMSIZE]
                       [--playerslist PLAYERSLIST [PLAYERSLIST ...]]

optional arguments:
  -h, --help            show this help message and exit
  --teamsize TEAMSIZE   max team size - integer non negative preferably
  --playerslist PLAYERSLIST [PLAYERSLIST ...]
                        space delimited list of players to be divided in to
                        teams
```
```bash

(venv) C:\Users\gq\PycharmProjects\dot-team-builder>python team-builder.py --teamsize 2 --playerslist Ben GQ Thomas Maksym Caleb Dean

Generating teams with team size of 2

Team 0:
Maksym, Thomas

Team 1:
Ben, Dean

Team 2:
Caleb, GQ
```


# Tournament Formats
Game to 11, win by 2<br>
Gentleman's serves - should be returnable

# if 2 teams do best of 5 or whatever you agree on

# if 3 teams do round robin
- 0 vs 1
- 1 vs 2
- 2 vs 0

Two best records or points play championship match

# if 4 teams do 0 vs 1 and 2 vs 3
-  Winner of (0 vs 1) Plays Winner of (2 vs 3)
-  Loser of (0 vs 1) Plays loser of (2 vs 3) for redemption
- Winner of each of the above faces off in the championship for all the marbles

# References
https://spikeball.com/pages/official-rules