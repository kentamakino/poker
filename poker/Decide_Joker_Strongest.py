# 最強役となるようなJOKERを決定する（middle,bottom用）
import collections


def decide_joker_strongest(card):
    # jokerの数をカウント
    joker_count = 0

    for i in range(0, 5):
        if card[i]['number'] == 99:
            joker_count += 1

    # ジョーカーが2枚の処理
    '''
    【判定条件】
    JOKER以外の3枚について
    ペアがある⇒クワッズ
    ペアがない⇒　スートが同じ⇒　すべてT以上orA⇒ロイヤル
                           　トップーボトムが4以下⇒ストフラ
                          　 それ以外⇒フラッシュ
            ⇒　トップーボトムが4以下　⇒ストレート
                                  ⇒スリーカード    
    '''

    if joker_count == 2:
        cards = sorted(card, key=lambda x: x['number'])

        if cards[0]['number'] == cards[1]['number'] or cards[1]['number'] == cards[2]['number']:  # ペア判定
            cards[3] = cards[1]
            cards[4] = cards[1]
            return cards  # クワッズ

        elif cards[0]['symbol'] == cards[1]['symbol'] == cards[2]['symbol']:  # スート判定
            if cards[0]['number'] >= 10 or cards[0]['number'] == 1 and cards[1]['number'] >= 10:  # ロイヤル判定

                a = []
                for i in range(0, 3):
                    a.append(cards[i]['number'])
                b = [1, 10, 11, 12, 13]
                diff_list = set(a) ^ set(b)

                cards[3]['number'] = list(diff_list)[0]
                cards[3]['symbol'] = cards[0]['symbol']
                cards[4]['number'] = list(diff_list)[1]
                cards[4]['symbol'] = cards[0]['symbol']
                return cards  # royal

            elif (cards[2]['number'] - cards[0]['number']) <= 4:
                a = []
                for i in range(0, 3):
                    a.append(cards[i]['number'])
                b = list(range(cards[0]['number'], cards[0]['number'] + 5))
                diff_list = set(a) ^ set(b)

                cards[3]['number'] = list(diff_list)[0]
                cards[3]['symbol'] = cards[0]['symbol']
                cards[4]['number'] = list(diff_list)[1]
                cards[4]['symbol'] = cards[0]['symbol']

                return cards  # ストフラ
            else:
                a = []
                for i in range(0, 3):
                    a.append(cards[i]['number'])
                b = list(range(1, 14))
                diff_list = list(set(a) ^ set(b))
                diff_list = sorted(diff_list, key=lambda x: x['number'])
                if list(diff_list)[0] == 1:
                    cards[3]['number'] = list(diff_list)[0]
                    cards[3]['symbol'] = cards[0]['symbol']
                    cards[4]['number'] = list(diff_list)[9]
                    cards[4]['symbol'] = cards[0]['symbol']
                else:
                    cards[3]['number'] = list(diff_list)[8]
                    cards[3]['symbol'] = cards[0]['symbol']
                    cards[4]['number'] = list(diff_list)[9]
                    cards[4]['symbol'] = cards[0]['symbol']

                return cards  # フラッシュ
        else:
            if cards[0]['number'] >= 10 or cards[0]['number'] == 1 and cards[1]['number'] >= 10:  # Aハイストレート判定

                a = []
                for i in range(0, 3):
                    a.append(cards[i]['number'])
                b = [1, 10, 11, 12, 13]
                diff_list = set(a) ^ set(b)

                cards[3]['number'] = list(diff_list)[0]
                cards[3]['symbol'] = cards[0]['symbol']
                cards[4]['number'] = list(diff_list)[1]
                cards[4]['symbol'] = cards[0]['symbol']
                return cards  # Aハイストレート

            elif (cards[2]['number'] - cards[0]['number']) <= 4:
                a = []
                for i in range(0, 3):
                    a.append(cards[i]['number'])
                b = list(range(cards[0]['number'], cards[0]['number'] + 5))
                diff_list = set(a) ^ set(b)

                cards[3]['number'] = list(diff_list)[0]
                cards[3]['symbol'] = cards[0]['symbol']
                cards[4]['number'] = list(diff_list)[1]
                cards[4]['symbol'] = cards[0]['symbol']

                return cards  # ストレート
            else:
                cards[3]['number'] = cards[2]['number']
                cards[3]['symbol'] = cards[0]['symbol']
                cards[4]['number'] = cards[2]['number']
                cards[4]['symbol'] = cards[0]['symbol']
                return cards  # トリップス

    # ジョーカーが1枚の処理

    elif joker_count == 1:

        cards = sorted(card, key=lambda x: x['number'])

        a = []
        for i in range(0, 4):
            a.append(cards[i]['number'])
        number_of_element = len(collections.Counter(a))  # 何種類の数字が含まれているか=ペア有無

        if number_of_element == 1:  # ジョーカーを除いて4カード
            if cards[0]['number'] == 1:

                cards[4]['number'] = 13
                cards[4]['symbol'] = cards[0]['symbol']
            else:
                cards[4]['number'] = 1
                cards[4]['symbol'] = cards[0]['symbol']
            return cards  # クワッズ

        elif number_of_element == 2:  # ジョーカーを除いて2ペアor3カード
            if cards[0]['number'] == cards[1]['number'] and cards[2]['number'] == cards[3]['number']:

                if cards[0]['number'] == 1:
                    cards[4]['number'] = cards[0]['number']
                    cards[4]['symbol'] = cards[0]['symbol']
                    return cards  # フルハウス
                else:
                    cards[4]['number'] = cards[3]['number']
                    cards[4]['symbol'] = cards[0]['symbol']
                    return cards  # フルハウス
            else:
                b = collections.Counter(a)
                cards[4]['number'] = b.most_common()[0][0]  # 最も頻度の高い数字＝3カードの数字
                cards[4]['symbol'] = cards[0]['symbol']
                return cards  # クワッズ

        elif number_of_element == 3:  # ジョーカーを除いて1ペア
            b = collections.Counter(a)
            cards[4]['number'] = b.most_common()[0][0]  # 最も頻度の高い数字＝ペアの数字
            cards[4]['symbol'] = cards[0]['symbol']
            return cards  # スリーカード

        elif cards[0]['symbol'] == cards[1]['symbol'] == cards[2]['symbol'] == cards[3]['symbol']:  # スート判定

            if cards[0]['number'] >= 10 or cards[0]['number'] == 1 and cards[1]['number'] >= 10:  # ロイヤル判定

                b = [1, 10, 11, 12, 13]
                diff_list = set(a) ^ set(b)

                cards[4]['number'] = list(diff_list)[0]
                cards[4]['symbol'] = cards[0]['symbol']
                return cards  # royal

            elif (cards[3]['number'] - cards[0]['number']) <= 4:

                b = list(range(cards[0]['number'], cards[0]['number'] + 5))
                diff_list = set(a) ^ set(b)

                cards[4]['number'] = list(diff_list)[0]
                cards[4]['symbol'] = cards[0]['symbol']

                return cards  # ストフラ
            else:

                b = list(range(1, 14))
                diff_list = set(a) ^ set(b)

                if list(diff_list)[0] == 1:
                    cards[4]['number'] = list(diff_list)[0]
                    cards[4]['symbol'] = cards[0]['symbol']

                else:
                    cards[4]['number'] = list(diff_list)[8]
                    cards[4]['symbol'] = cards[0]['symbol']
                return cards  # フラッシュ

        else:  # ジョーカーを除いてハイカードかつオフスート
            if cards[0]['number'] >= 10 or cards[0]['number'] == 1 and cards[1]['number'] >= 10:  # Aハイストレート判定

                b = [1, 10, 11, 12, 13]
                diff_list = set(a) ^ set(b)

                cards[4]['number'] = list(diff_list)[0]
                cards[4]['symbol'] = cards[0]['symbol']
                return cards  # Aハイストレート

            elif (cards[3]['number'] - cards[0]['number']) <= 4:

                b = list(range(cards[0]['number'], cards[0]['number'] + 5))
                diff_list = set(a) ^ set(b)

                cards[4]['number'] = list(diff_list)[0]
                cards[4]['symbol'] = cards[0]['symbol']

                return cards  # ストレート
            else:
                if cards[0]['number'] == 1:
                    cards[4]['number'] = cards[0]['number']
                    cards[4]['symbol'] = cards[3]['symbol']

                else:
                    cards[4]['number'] = cards[3]['number']
                    cards[4]['symbol'] = cards[3]['symbol']

                return cards  # ワンペア

    else:
        return card


'''
【判定条件】
JOKER以外の4枚について
スートが一致⇒ロイヤルorストフラorフラッシュ（JOKER2枚と同様に判別）
スートが不一致⇒ペアがある　
                    　 3カードor4カード⇒クワッズ
            　         2ペア⇒フルハウス
            　         ワンペア⇒トリップス
             ペアがない
                    　 差分が4以下⇒ストレート(Aハイストレートは別途判定)
                       それ以外⇒ワンペア

'''

'''
    【JOKER2枚の時の最強ハンド】
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
【JOKER1枚の時の最強ハンド】
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