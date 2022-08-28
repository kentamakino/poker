import itertools
import random

from Cal_Score import calc_score
import util


def calc_expected_score(cards):
    """
    :param cards: list of 13 number
    :return: expected score
    """

    total_score = 0

    unplaced_positions = [index for index, val in enumerate(cards) if val == -1]
    assert len(unplaced_positions) == 2
    placed_cards = [util.convert_number_to_card(v) for v in cards]
    # ダミーカードを追加
    placed_cards.append(
        {'number': 0, 'symbol': 'None'}
    )
    placed_cards.append(
        {'number': 0, 'symbol': 'None'}
    )

    calculated_hand_count = 0
    for possible_hand in util.list_possible_next_hands(cards):
        calculated_hand_count += 1
        score = 0
        hand = [util.convert_number_to_card(v) for v in possible_hand]
        # 配られた3枚の手札の中から使用する2枚を選ぶ
        for use_cards in itertools.combinations(hand, 2):
            placed_cards[unplaced_positions[0]] = use_cards[0]
            placed_cards[unplaced_positions[1]] = use_cards[1]
            score = max(score, calc_score(placed_cards[10:], placed_cards[5:10], placed_cards[:5]))
            # カードの置き方２パターン両方計算する
            placed_cards[unplaced_positions[0]] = use_cards[1]
            placed_cards[unplaced_positions[1]] = use_cards[0]
            score = max(score, calc_score(placed_cards[10:], placed_cards[5:10], placed_cards[:5]))
        total_score += score

    return total_score / calculated_hand_count


def calc_expected_score_random(cards, num_calc):
    """
    :param cards: list of 13 number
    :return: expected score
    """

    total_score = 0

    unplaced_positions = [index for index, val in enumerate(cards) if val == -1]
    assert len(unplaced_positions) == 2
    placed_cards = [util.convert_number_to_card(v) for v in cards]
    # ダミーカードを追加
    placed_cards.append(
        {'number': 0, 'symbol': 'None'}
    )
    placed_cards.append(
        {'number': 0, 'symbol': 'None'}
    )

    calculated_hand_count = 0
    possible_hands = [v for v in util.list_possible_next_hands(cards)]
    for possible_hand in random.sample(possible_hands, num_calc):
        calculated_hand_count += 1
        score = 0
        hand = [util.convert_number_to_card(v) for v in possible_hand]
        # 配られた3枚の手札の中から使用する2枚を選ぶ
        for use_cards in itertools.combinations(hand, 2):
            placed_cards[unplaced_positions[0]] = use_cards[0]
            placed_cards[unplaced_positions[1]] = use_cards[1]
            score = max(score, calc_score(placed_cards[10:], placed_cards[5:10], placed_cards[:5]))
            # カードの置き方２パターン両方計算する
            placed_cards[unplaced_positions[0]] = use_cards[1]
            placed_cards[unplaced_positions[1]] = use_cards[0]
            score = max(score, calc_score(placed_cards[10:], placed_cards[5:10], placed_cards[:5]))
        total_score += score

    return total_score / calculated_hand_count
