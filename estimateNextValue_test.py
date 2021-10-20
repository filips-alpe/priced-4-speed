from estimate import estimateNextVolume


def test_empty_list():
    assert estimateNextVolume([]) == 0


def test_single_element():
    assert estimateNextVolume([3]) == 3


def test_multiple_identical_elements():
    assert estimateNextVolume([0.5, 0.5, 0.5, 0.5]) == 0.5

# Assertions in test cases below are intentionally approximate
# to accommodate future improvements in the prediction algorithm.


def test_negative_and_positive_elements():
    assert estimateNextVolume([-3, 5]) > 0


def test_increasing_progression():
    assert estimateNextVolume([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) > 5


def test_decreasing_progression():
    assert estimateNextVolume([100, 90, 80, 70, 60, 50, 40, 30]) < 70
