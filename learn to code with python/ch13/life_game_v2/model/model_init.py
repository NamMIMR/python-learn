from typing import List
import sys
sys.path.append('../..')
import life_game_v2
from life_game_v2.model import patterns


def setup_model(height: int, width: int, pattern: str = 'default') -> List[List[int]]:
    pass


if __name__ == "__main__":
    model = setup_model(100, 100)