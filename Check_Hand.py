# 役判定
def check_hand(card):
    # ペア数
    pair_count = 0
    # 同じ数字のカウント
    match_count = 0
    # 同じ数字の枚数(3カード,4カードチェック用)
    match_number = 0
    # フラッシュの有無フラグ
    flash_flag = True
    # ストレートの有無フラグ
    straight_flag = True

    # 数字の昇順に並び替える
    cards = sorted(card, key=lambda x: x['number'])

    # 比較チェックループ
    for i in range(1, 5):
        # 前の数字が同じかチェック
        if cards[i]['number'] == cards[i - 1]['number']:
            match_count += 1
            # 最終ループチェック
            if i == 4:
                if match_count == 1:
                    pair_count += 1
                # 3カード以上の場合
                elif match_count > 1:
                    match_number = match_count + 1
        else:
            # 違う数字の場合
            if match_count == 1:
                pair_count += 1
            # 3カード以上の場合
            elif match_count > 1:
                match_number = match_count + 1
            match_count = 0
        # 同じマークが続いているかチェック
        if flash_flag == True and cards[i]['symbol'] != cards[i - 1]['symbol']:
            flash_flag = False
        # 数字が連続しているかチェック
        if straight_flag == True and cards[i]['number'] != cards[i - 1]['number'] + 1:
            if cards[i]['number'] != 10 or cards[i - 1]['number'] != 1:
                straight_flag = False

            # 最終手札チェック
    if straight_flag == True and flash_flag == True:
        if cards[0]['number'] == 1 and cards[4]['number'] == 13:
            # ロイヤルストレートフラッシュ
            hand = 'ロイヤル\nストレートフラッシュ'
            hand_strength = 9
        else:
            # ストレートフラッシュ
            hand = 'ストレートフラッシュ'
            hand_strength = 8


    elif match_number > 2:
        if match_number == 4:
            # 4カード
            hand = '4カード'
            hand_strength = 7
        else:
            if pair_count > 0:
                # フルハウス
                hand = 'フルハウス'
                hand_strength = 6
            else:
                # 3カード
                hand = '3カード'
                hand_strength = 3
    elif flash_flag == True:
        # フラッシュ
        hand = 'フラッシュ'
        hand_strength = 5
    elif straight_flag == True:
        # ストレート
        hand = 'ストレート'
        hand_strength = 4
    elif pair_count > 0:
        if pair_count > 1:
            # 2ペア
            hand = '2ペア'
            hand_strength = 2
        else:
            # 1ペア
            hand = '1ペア'
            hand_strength = 1
    else:
        # なし
        hand = 'ぶた'
        hand_strength = 0

    return hand, hand_strength, cards


def comparison_hands(card_upper, card_lower):
    # ハンドの強さ比較
    strength_upper = check_hand(card_upper)[1]

    strength_lower = check_hand(card_lower)[1]

    # 異なる場合はTrue or Falseを返す
    if strength_upper < strength_lower:
        return True
    if strength_upper > strength_lower:
        return False

    # ハンドランクが異なる場合の処理

    # 数字だけの降順配列に成形、A＝14に置換
    card_upper_numbers = []
    card_lower_numbers = []

    for i in range(0, 5):
        card_upper_number = card_upper[4 - i]['number']
        if card_upper_number == 1:
            card_upper_number = 14
        card_upper_numbers.append(card_upper_number)

        card_lower_number = card_lower[4 - i]['number']
        if card_lower_number == 1:
            card_lower_number = 14
        card_lower_numbers.append(card_lower_number)

    card_upper_numbers = sorted(card_upper_numbers, key=lambda x: x, reverse=True)
    card_lower_numbers = sorted(card_lower_numbers, key=lambda x: x, reverse=True)

    # ①ハイカード(=0) ソートの比較
    if strength_upper == 0:

        if card_lower_numbers >= card_upper_numbers:
            return True

        else:
            return False



    # ②ワンペア(=1)　ペアの比較⇒残り3桁のソート比較
    elif strength_upper == 1:

        dup_upper = list({x for x in card_upper_numbers if card_upper_numbers.count(x) > 1})
        dup_lower = list({x for x in card_lower_numbers if card_lower_numbers.count(x) > 1})

        # ペアの数字比較
        if dup_upper < dup_lower:
            return True
        elif dup_upper > dup_lower:
            return False

        else:

            # ペアの数字が同じ場合のキッカー比較
            if card_upper_numbers <= card_lower_numbers:
                return True
            else:
                return False

    # ③2ペア（=2）ペアの比較⇒ペアの数字比較⇒残り1桁の比較
    elif strength_upper == 2:

        dup_upper = list({x for x in card_upper_numbers if card_upper_numbers.count(x) > 1})
        dup_lower = list({x for x in card_lower_numbers if card_lower_numbers.count(x) > 1})

        # ペアの数字比較
        if dup_upper < dup_lower:
            return True
        elif dup_upper > dup_lower:
            return False

        else:

            # ペアの数字が同じ場合のキッカー比較
            if card_upper_numbers <= card_lower_numbers:
                return True
            else:
                return False

    # ④3カード（=3）3カードの比較⇒残りの2桁ソート比較
    elif strength_upper == 3:

        dup_upper = list({x for x in card_upper_numbers if card_upper_numbers.count(x) > 1})
        dup_lower = list({x for x in card_lower_numbers if card_lower_numbers.count(x) > 1})

        # ペアの数字比較
        if dup_upper < dup_lower:
            return True
        elif dup_upper > dup_lower:
            return False

        else:

            # ペアの数字が同じ場合のキッカー比較
            if card_upper_numbers <= card_lower_numbers:
                return True
            else:
                return False



    # ⑤ストレート(=4)　最小値が2同士の場合は、最大値比較⇒それ以外は最小値比較
    elif strength_upper == 4:

        if min(card_upper_numbers) == min(card_lower_numbers) == 2 & max(card_upper_numbers) == 6 & max(
                card_lower_numbers) == 14:
            return False
        elif min(card_upper_numbers) <= min(card_lower_numbers):
            return True
        else:
            return False

    # ⑥フラッシュ(=5)　ソートの比較
    elif strength_upper == 5:

        if card_lower_numbers >= card_upper_numbers:
            return True

        else:
            return False

    # フルハウス(=6)　3カードの比較⇒ペアの比較
    elif strength_upper == 6:

        dup_upper = list({x for x in card_upper_numbers if card_upper_numbers.count(x) > 2})
        dup_lower = list({x for x in card_lower_numbers if card_lower_numbers.count(x) > 2})

        # ペアの数字比較
        if dup_upper < dup_lower:
            return True
        elif dup_upper > dup_lower:
            return False

        else:

            # ペアの数字が同じ場合のキッカー比較
            if card_upper_numbers <= card_lower_numbers:
                return True
            else:
                return False

    # ⑧4カード(=7)　4カードの比較⇒残り1桁の比較
    elif strength_upper == 7:

        dup_upper = list({x for x in card_upper_numbers if card_upper_numbers.count(x) > 3})
        dup_lower = list({x for x in card_lower_numbers if card_lower_numbers.count(x) > 3})

        # ペアの数字比較
        if dup_upper < dup_lower:
            return True
        elif dup_upper > dup_lower:
            return False
        else:

            # ペアの数字が同じ場合のキッカー比較
            if min(card_upper_numbers) <= min(card_lower_numbers):
                return True
            else:
                return False

    # ⑨ストレートフラッシュ(=8)⇒最大値の比較
    elif strength_upper == 8:

        if min(card_upper_numbers) == min(card_lower_numbers) == 2 & max(card_upper_numbers) == 6 & max(
                card_lower_numbers) == 14:
            return False
        elif min(card_upper_numbers) <= min(card_lower_numbers):
            return True
        else:
            return False

    # ロイヤルストレートフラッシュ(=9)⇒ドロー
    elif strength_upper == 9:
        return True
