from typing import List


def estimateNextVolume(volumes: List[float]) -> float:
    # Very simple for now - computes the average volume in the last hour.
    # Could be improved, possibly significantly - for example, by an algorithm
    # that puts more weight on the recent volumes and less on an older ones.
    numOfItems = len(volumes)
    return sum(volumes) / numOfItems if numOfItems > 0 else 0
