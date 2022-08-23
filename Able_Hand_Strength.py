import collections


def able_hand_strength(card):
    # jokerの数をカウント
    joker_count = 0

    for i in range(0, 5):
        if card[i]['number'] == 99:
            joker_count += 1

    cards = sorted(card, key=lambda x: x['number'])

    able_hand_strength = [False, False, False, False, False, False, False, False, False, False]

    if joker_count == 2:

        a = []
        for i in range(0, 3):
            a.append(cards[i]['number'])
        number_of_element = len(collections.Counter(a))  # 何種類の数字が含まれているか=ペア有無

        if number_of_element == 1:
            able_hand_strength[3] = True
            able_hand_strength[6] = True
            able_hand_strength[7] = True

        if number_of_element == 2:
            able_hand_strength[1] = True
            able_hand_strength[2] = True
            able_hand_strength[3] = True
            able_hand_strength[6] = True
            able_hand_strength[7] = True

        if number_of_element == 3:
            able_hand_strength[0] = True
            able_hand_strength[1] = True
            able_hand_strength[2] = True
            able_hand_strength[3] = True

            if cards[0]['number'] >= 10 or cards[0]['number'] == 1 and cards[1]['number'] >= 10:
                able_hand_strength[4] = True
            if (cards[2]['number'] - cards[0]['number']) <= 4:
                able_hand_strength[4] = True

            if cards[0]['symbol'] == cards[1]['symbol'] == cards[2]['symbol']:
                able_hand_strength[5] = True
                if cards[0]['number'] >= 10 or cards[0]['number'] == 1 and cards[1]['number'] >= 10:  # ロイヤル判定
                    able_hand_strength[9] = True
                if (cards[2]['number'] - cards[0]['number']) <= 4:
                    able_hand_strength[8] = True

        return able_hand_strength

    if joker_count == 1:

        a = []
        for i in range(0, 4):
            a.append(cards[i]['number'])
        number_of_element = len(collections.Counter(a))  # 何種類の数字が含まれているか=ペア有無

        if number_of_element == 1:
            able_hand_strength[7] = True

        if number_of_element == 2:
            able_hand_strength[6] = True

            if cards[0]['number'] == cards[1]['number'] and cards[2]['number'] == cards[3]['number']:
                able_hand_strength[2] = True
            else:
                able_hand_strength[3] = True
                able_hand_strength[7] = True

        if number_of_element == 3:
            able_hand_strength[1] = True
            able_hand_strength[2] = True
            able_hand_strength[3] = True

        if number_of_element == 4:
            able_hand_strength[0] = True
            able_hand_strength[1] = True

            if cards[0]['number'] >= 10 or cards[0]['number'] == 1 and cards[1]['number'] >= 10:  # Aハイストレート判定
                able_hand_strength[4] = True
            if (cards[3]['number'] - cards[0]['number']) <= 4:
                able_hand_strength[4] = True

            if cards[0]['symbol'] == cards[1]['symbol'] == cards[2]['symbol'] == cards[3]['symbol']:
                able_hand_strength[5] = True
                if cards[0]['number'] >= 10 or cards[0]['number'] == 1 and cards[1]['number'] >= 10:  # ロイヤル判定
                    able_hand_strength[9] = True
                if (cards[3]['number'] - cards[0]['number']) <= 4:
                    able_hand_strength[8] = True
        return able_hand_strength




'''
【中段JOKERの決定条件】
①中段の最強ハンドを作る
②中下段比較⇒下段が強い場合はOK
③中段が強い場合は、hand_strengthの作成可否配列
0:〇　ハイカード
1:〇　ワンペア
2:〇　2ペア
3:×　トリップス
4:×　ストレート
5:〇　フラッシュ
6:×　フルハウス
7:〇　4カード
8:〇　ストフラ
9:×　ロイヤル
④下段のhand_strengthが中段で作成できる場合は、そのhand_strengthで最弱となるようなJOKERに決定する(トリップス、ワンペアは詳細要件検討要)
⑤　④の作成後に中下段比較⇒下段が強い場合はOK
⑥　④⑤が不可の場合は、下段のhand_strength未満で中段が作成可能なhand_strengthの最大値の最強ハンドを作成
'''

'''
JOKER2枚の時の判定

0:　ハイカード
3種類
1:　ワンペア
3種類か2種類
2:　2ペア
3種類か2種類
3:　トリップス
条件なし
4:　ストレート
差分が４以下＋Aハイストレートの判定
5:　フラッシュ
スートが一致
6:　フルハウス
2種類か1種類
7:　4カード
2種類、1種類
8:　ストフラ
スートが一致＋差分が4以下
9:　ロイヤル
スートが一致＋Aハイストレート
'''



'''
JOKER1枚の時の判定

0:　ハイカード
4
1:　ワンペア
3,4
2:　2ペア
3,2(2,2の場合のみ)

3:　トリップス
3,2(1,3の場合のみ)

4:　ストレート
4
差分が４以下＋Aハイストレートの判定

5:　フラッシュ
4
スートが一致

6:　フルハウス
2
7:　4カード
2(1,3のみ)、1

8:　ストフラ
4
スートが一致＋差分が4以下
9:　ロイヤル
4
スートが一致＋Aハイストレート

'''
