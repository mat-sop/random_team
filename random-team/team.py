from typing import List
import numpy as np


def filter_bots(members: List) -> List:
    return [member for member in members if not member.bot]


def split_players(players: List, teams_number: int = 2) -> List[List]:
    print(players)
    # players = np.array(players)
    # np.random.shuffle(players)
    # print(players)
    # teams = np.array_split(players, teams_number)
    # print(teams)
    # return [team.tolist() for team in teams]
    return players


def format_teams(teams: List[List[str]]) -> str:
    output = ''
    template ='''
    Team {number}:
        {members}

    '''
    i = 1
    for team in teams:
        output += template.format(number=i, members=', '.join(team))
        i += 1
    return output
