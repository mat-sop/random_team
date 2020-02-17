from typing import List

import numpy as np


def split_members(members: List, teams_number: int) -> List[List]:
    filtered_members = filter_bots(members)
    names = [member.name for member in filtered_members]
    return random_split_list(names, teams_number)


def filter_bots(members: List) -> List:
    return [member for member in members if not member.bot]


def random_split_list(elements: List, sublists_number: int = 2) -> List[List]:
    elements_copy = elements.copy()
    np.random.shuffle(elements_copy)
    sublists = np.array_split(elements_copy, sublists_number)
    return [sublist.tolist() for sublist in sublists]


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
