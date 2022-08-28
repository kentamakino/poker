import random
import math
import itertools

DECK = tuple(range(54))


def get_cards(num_card):
    return random.sample(DECK, num_card)


def get_cards_with_position(num_card):
    """
    :param num_card:
    :return: List of number. length: 15. "-1" means blank position.
    """
    numbers = random.sample(DECK, num_card)
    retval = [numbers[i] if len(numbers) > i else -1 for i in range(15)]
    random.shuffle(retval)
    return retval


def get_card_number(number):
    return number % 13 + 1


def get_suite_name(number):
    suite_number = number // 13
    if suite_number == 0:
        return "Hearts"
    elif suite_number == 1:
        return "Clubs"
    elif suite_number == 2:
        return "Spades"
    else:
        return "Diamonds"


def convert_number_to_card(number):
    return {
        "number": get_card_number(number),
        "symbol": get_suite_name(number)
    }


def get_possible_next_hands_num(used_card_num, *, num_hands=3):
    num_deck_cards = len(DECK) - used_card_num
    return int(math.factorial(num_deck_cards) / math.factorial(num_deck_cards - num_hands) / math.factorial(num_hands))


def list_possible_next_hands(used_card_list, *, num_hands=3):
    current_deck = set(DECK) - set(used_card_list)
    for hand in itertools.combinations(current_deck, num_hands):
        yield hand
