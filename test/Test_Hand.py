from poker.Decide_Joker_Strongest import decide_joker_strongest


def test_royal_straight_flush():
    card31 = {'number': 99, 'symbol': 'Clubs'}
    card32 = {'number': 99, 'symbol': 'Clubs'}
    card33 = {'number': 11, 'symbol': 'Hearts'}
    card34 = {'number': 13, 'symbol': 'Hearts'}
    card35 = {'number': 1, 'symbol': 'Hearts'}
    card3 = [card31, card32, card33, card34, card35]
    card3_strongest = decide_joker_strongest(card3)
    sorted_card3_strongest = sorted(card3_strongest, key=lambda x: x['number'])
    assert sorted_card3_strongest[0]['number'] == 1
    assert sorted_card3_strongest[1]['number'] == 10
    assert sorted_card3_strongest[2]['number'] == 11
    assert sorted_card3_strongest[3]['number'] == 12
    assert sorted_card3_strongest[4]['number'] == 13
    for card in sorted_card3_strongest:
        assert card['symbol'] == 'Hearts'

# 0:　ハイカード 1:　ワンペア 2:　2ペア 3:　トリップス 4:　ストレート 5:　フラッシュ 6:　フルハウス 7:　4カード 8:　ストフラ 9:　ロイヤル
