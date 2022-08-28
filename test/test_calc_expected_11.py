from poker.calc_expected_11 import *


def test_calc_expected_score():
    cards = [2, 15, 28, 41, 1]
    cards.extend([3, 16, 5, 6, 30])
    cards.extend([-1, -1, 31])
    expected_score = calc_expected_score(cards)
    print(expected_score)
    assert expected_score > 0


def test_calc_expected_score_random():
    cards = [2, 15, 28, 41, 1]
    cards.extend([3, 16, 5, 6, 30])
    cards.extend([-1, -1, 31])
    expected_score = calc_expected_score_random(cards, 1000)
    print(expected_score)
    assert expected_score >= 0
