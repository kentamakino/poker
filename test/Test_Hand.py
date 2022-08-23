from Decide_Joker_Strongest import decide_joker_strongest
from Decede_Joker_Middle_and_Bottom import decide_joker_middle_and_bottom

card21 = {'number': 5, 'symbol': 'Hearts'}
card22 = {'number': 2, 'symbol': 'Hearts'}
card23 = {'number': 7, 'symbol': 'Hearts'}
card24 = {'number': 99, 'symbol': 'Joker'}
card25 = {'number': 9, 'symbol': 'Hearts'}

card2 = [card21, card22, card23, card24, card25]

card31 = {'number': 12, 'symbol': 'Hearts'}
card32 = {'number': 4, 'symbol': 'Hearts'}
card33 = {'number': 2, 'symbol': 'Clubs'}
card34 = {'number': 5, 'symbol': 'Hearts'}
card35 = {'number': 1, 'symbol': 'Clubs'}

card3 = [card31, card32, card33, card34, card35]


#print(decide_joker_middle_and_bottom(card2, card3))

card3_strongest = decide_joker_strongest(card3)
print(card3)


# 0:　ハイカード 1:　ワンペア 2:　2ペア 3:　トリップス 4:　ストレート 5:　フラッシュ 6:　フルハウス 7:　4カード 8:　ストフラ 9:　ロイヤル
