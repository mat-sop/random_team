from typing import List
import numpy as np


def split_players(players: List[str], teams_number: int = 2) -> List[List[str]]:
    players = np.array(players)
    np.random.shuffle(players)
    teams = np.array_split(players, teams_number)
    return [team.tolist() for team in teams]
