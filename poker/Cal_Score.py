# 上段の点数計算
def score_top(card):
    cards = []
    for i in range(0, 5):
        card_number = card[4 - i]['number']
        if card_number == 1:
            card_number = 14
        cards.append(card_number)

    cards = sorted(cards, key=lambda x: x)

    if cards[2] == cards[3] == cards[4]:
        return cards[2] + 8

        # 222:10~AAA:22

    elif cards[2] == cards[3] or cards[3] == cards[4]:

        # 66:1~AA:9
        dup_top = list({x for x in cards if cards.count(x) > 1})
        if dup_top[0] >= 6:
            return dup_top[0] - 5
        else:
            return 0

    else:
        return 0


# 中段のスコア計算
def score_middle(card_middle_strength):
    score_middle_table = [0, 0, 0, 2, 4, 8, 12, 20, 30, 50]
    return score_middle_table[card_middle_strength]


# 下段のスコア計算
def score_bottom(card_bottom_strength):
    score_bottom_table = [0, 0, 0, 0, 2, 4, 6, 10, 15, 25]
    return score_bottom_table[card_bottom_strength]
