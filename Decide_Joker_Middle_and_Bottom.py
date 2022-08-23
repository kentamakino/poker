import collections
from Decide_Joker_Strongest import decide_joker_strongest
from Check_Hand import check_hand, comparison_hands
from Able_Hand_Strength import able_hand_strength


def decide_joker_middle_and_bottom(card2, card3):

    global card3_decided, card2_strongest, card2_decided

    # jokerの数をカウント
    joker_count_card2 = 0
    joker_count_card3 = 0

    for i in range(0, 5):
        if card2[i]['number'] == 99:
            joker_count_card2 += 1

        if card3[i]['number'] == 99:
            joker_count_card3 += 1

    if joker_count_card3 >= 1:  # card3のJOKERを決定
        card3_decided = decide_joker_strongest(card3)
    else:
        card3_decided = card3

    if joker_count_card2 == 0:  # 中段にJOKERがない場合は終了
        card2_decided = card2
        return card2_decided, card3_decided

    if joker_count_card2 >= 1:  # 中段にJOKERがある場合

        # 中段最強ハンドを作成して下段のほうが強ければ終了
        card2_strongest = decide_joker_strongest(card2)
        if comparison_hands(card2_strongest, card3_decided):
            card2_decided = card2_strongest
            return card2_decided, card3_decided

        else:  # 下段より中段最強ハンドが強い場合の処理

            card3_strength = check_hand(card3_decided)[1]

            card2_list = []

            for i in range(0, 5):
                card = card2[4 - i]['number']
                if card == 1:
                    card = 14

                card2_list.append(card)
            print(card2_list)

            card3_list = []
            for i in range(0, 5):
                print(i)
                card = card3_decided[4 - i]['number']
                if card == 1:
                    card = 14
                card3_list.append(card)
            print(card3_list)

            card2_list = sorted(card2_list, key=lambda x: x, reverse=True)
            card3_list = sorted(card3_list, key=lambda x: x, reverse=True)

            if able_hand_strength(card2)[card3_strength]:

                if card3_strength == 0:

                    all_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
                    diff_list = list(set(card2_list) ^ set(all_number))
                    diff_list = sorted(diff_list, key=lambda x: x, reverse=True)

                    for card in diff_list:
                        card2_list.append(card)
                        card2_list = sorted(card2_list, key=lambda x: x, reverse=True)
                        if card2_list >= card3_list:
                            card2[4] = card
                            return card2, card3_decided
                    card2[4] = diff_list[0]
                    return card2, card3_decided

            else:

                return card2_decided, card3_decided


'''
JOKER1枚
    ハイカード:0
    １，１，１，１
    キッカーの最大値比較⇒ＯＫの場合　Ｊ＝下段キッカーの最大値　⇒ＮＧの場合　Ｊ＝下段キッカーの最大値ー１
    
    
    ワンペア:1
    
    ※Aの扱いに注意
    
    １，１，１，１⇒強い順にJに代入
    下段のペアの数字＞中段のペアの数字⇒　J＝代入した数字
    下段のペアの数字＝中段のペアの数字⇒キッカー比較
        OKの場合はJ＝代入した数字
        NGの場合はJ＝次に強い数字
    下段のペアの数字＜中段のペアの数字⇒J＝代入した数字
    
    １，１，２
    下段のペアの数字＞中段のペアの数字⇒　J＝一番強いキッカー
    下段のペアの数字＝中段のペアの数字⇒キッカーの最大値を比較　⇒OKの場合J=下段キッカーの最大値を入力⇒NGの場合はJ＝下段キッカーの最大値ー１
    

    
    
    ツーペア:2
    １，１，２　J＝弱いほうの１
    ２，２　J＝一番弱いキッカー
    スリーカード:3
    １，３　J＝一番弱いキッカー
    １，１，２　J＝２の数字
    
    ストレート:4
    差分＝４⇒ J=ガットの間
    差分＝３⇒ J＝ボトムー１
    AハイストレートはJ＝ガットの間
    
    フラッシュ:5
    弱い数字を入力⇒ソートして差分が4以下の場合は、次に弱い数字を入力⇒ソートして差分が4以下の場合は次に弱い数字を入力
    
    フルハウス:6
    1,3　⇒　J＝1の数字
    2,2 ⇒　J＝弱い方

    フォーカード:7
    1,3⇒　J＝3の数字
    0.4⇒　J＝２（2222の時は3）

    ストフラ:8
    差分＝４⇒ J=ガットの間
    差分＝３⇒ J＝ボトムー１
    
    ロイヤル:9
    
'''
