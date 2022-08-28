from poker.util import *


def test_get_cards():
    num_cards = 5
    cards1 = get_cards(num_cards)
    cards2 = get_cards(num_cards)
    assert len(cards1) == num_cards
    assert len(tuple(cards1)) == num_cards
    assert len(cards2) == num_cards
    assert len(tuple(cards2)) == num_cards


def test_get_card_number():
    card = 0
    assert get_card_number(card) == 1

    card = 12
    assert get_card_number(card) == 13

    card = 13
    assert get_card_number(card) == 1


def test_get_suite_name():
    card = 0
    assert get_suite_name(card) == 'Hearts'

    card = 12
    assert get_suite_name(card) == 'Hearts'

    card = 13
    assert get_suite_name(card) == 'Clubs'

    card = 30
    assert get_suite_name(card) == 'Spades'

    card = 49
    assert get_suite_name(card) == 'Diamonds'


def test_get_cards_with_position():
    for num_cards in range(1, 16):
        cards = get_cards_with_position(num_cards)
        assert len(cards) == 15
        assert len([v for v in cards if v >= 0]) == num_cards
        assert len([v for v in cards if v < 0]) == 15 - num_cards


def test_list_possible_next_hands():
    assert list_possible_next_hands(51) == 1
    assert list_possible_next_hands(48) == 20
    assert list_possible_next_hands(10) == 13244


def test_get_possible_next_hands_num():
    used_cards = list(range(40))
    hand_count = 0
    for hand in get_possible_next_hands_num(used_cards):
        assert len(hand) == 3
        assert min(hand) >= 40
        assert max(hand) <= 54
        hand_count += 1

    assert hand_count == list_possible_next_hands(len(used_cards))
