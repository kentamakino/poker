from Cal_Score import score_top, score_middle, score_bottom
from Check_Hand import check_hand, comparison_hands


def main(card_top, card_middle, card_bottom):
    if comparison_hands(card_top, card_middle) and comparison_hands(card_middle, card_bottom):
        score_total = score_top(check_hand(card_top)[2]) + score_middle(check_hand(card_middle)[1]) + score_bottom(
            check_hand(card_bottom)[1])
    else:
        score_total = 0
    return comparison_hands(card_top, card_middle), comparison_hands(card_middle, card_bottom), comparison_hands(
        card_top, card_middle) and comparison_hands(card_middle, card_bottom), check_hand(card_top)[1], \
           check_hand(card_middle)[1], check_hand(card_bottom)[1], score_top(check_hand(card_top)[2]), score_middle(
        check_hand(card_middle)[1]), score_bottom(check_hand(card_bottom)[1]), score_total


# 配置の設定
# 上段左上からcard11~card35

card11 = {'number': 1, 'symbol': 'Hearts'}
card12 = {'number': 1, 'symbol': 'Clubs'}
card13 = {'number': 1, 'symbol': 'Hearts'}
# card14,15は存在しないが便宜上設定
card14 = {'number': 0, 'symbol': 'None'}
card15 = {'number': 0.1, 'symbol': 'None'}

card1 = [card11, card12, card13, card14, card15]

card21 = {'number': 7, 'symbol': 'Hearts'}
card22 = {'number': 7, 'symbol': 'Clubs'}
card23 = {'number': 7, 'symbol': 'Hearts'}
card24 = {'number': 7, 'symbol': 'Hearts'}
card25 = {'number': 2, 'symbol': 'Hearts'}

card2 = [card21, card22, card23, card24, card25]

card31 = {'number': 8, 'symbol': 'Hearts'}
card32 = {'number': 8, 'symbol': 'Clubs'}
card33 = {'number': 8, 'symbol': 'Diamonds'}
card34 = {'number': 8, 'symbol': 'Spades'}
card35 = {'number': 9, 'symbol': 'Hearts'}

card3 = [card31, card32, card33, card34, card35]

# 結果表示
print('\n', '【各段のハンド配置】')
print('上段', card1)
print('中段', card2)
print('下段', card3, '\n')

print('【ハンドランク】', '\n', '(ハイカード:0,ワンペア:1,ツーペア:2,スリーカード:3,ストレート:4,フラッシュ:5,フルハウス:6,フォーカード:7,ストフラ:8,ロイヤル:9)', '\n')
print('上段ハンドランク:', main(card1, card2, card3)[3])
print('上段スコア:', main(card1, card2, card3)[6], '\n')
print('中段ハンドランク:', main(card1, card2, card3)[4])
print('中段スコア:', main(card1, card2, card3)[7], '\n')
print('下段ハンドランク:', main(card1, card2, card3)[5])
print('下段スコア:', main(card1, card2, card3)[8], '\n')

print('【ファウル判定】')
print('上中段ハンドランク順判定:', main(card1, card2, card3)[0])
print('中下段ハンドランク順判定:', main(card1, card2, card3)[1])
print('上中下段ハンドランク順判定:', main(card1, card2, card3)[2], '\n')

print('【トータルスコア】', '\n', main(card1, card2, card3)[9], '点')

'''
JOKER2枚の時の最強ハンド
ハイカード:0
×
ワンペア:1
×
ツーペア:2
×
スリーカード:3
ハイカードの時。トップ3カードが最強

ストレート:4
トップーボトム＜＝４かつペアがない時。差が４⇒ハイカード　差が３⇒ハイカード＋１　差が２⇒ハイカード＋２
フラッシュ:5
スートが3枚。上から空いている数字を入れる

フルハウス:6
×
フォーカード:7
ペアがあるとき

ストフラ:8
スート＋トップーボトム＜＝４の時

ロイヤル:9
すべてのカード＞Tかつスート
'''



'''
JOKER1枚の時の最強ハンド
ハイカード:0
×
ワンペア:1
ハイカードの時。トップカードワンペアが最強
ツーペア:2
×
スリーカード:3
ワンペアの時。トップスリーカードが最強

ストレート:4
保留

フラッシュ:5
スートが4枚。上から空いている数字を入れる

フルハウス:6
2ペアのとき

フォーカード:7
スリーカードの時

ストフラ:8
保留

ロイヤル:9
すべてのカード＞Tかつスート

'''
