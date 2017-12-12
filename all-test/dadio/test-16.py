chr_info = [chr(i - 32) for i in range(97, 123)]

code_char=['A','T','J','Q','K']
code_num=[0,1,2,3,4]


def get_first(cards):
    print(chr_info)
    for (index, card) in zip(range(0, len(cards)), cards):
        if card in chr_info:
            return index, card
        else:
            continue
    return None


def sort_cards(card_str):
    cards = [item for item in card_str]

    cards_1 = [item for item in cards if item not in chr_info]
    cards_2 = [item for item in cards if item in chr_info]
    dir_card_2={}

    for (i,card) in zip(range(len(cards_2)),cards_2):
        index=code_char.index(card)
        dir_card_2[card]=code_num[index]


    print(cards_1)
    print(cards_2)
    print(dir_card_2)
    print('-------------')

    cards_1 = sorted(cards_1, key=lambda x: ord(x), reverse=False)
    # print(cards_1)

    dir_card_2 = sorted(dir_card_2.items(), key=lambda x: (x[1]), reverse=False)
    print(dir_card_2)
    print('-----')

    card_first=dir_card_2[0][0]
    cards = [card_first] + cards_1
    for item in dir_card_2[1:]:
        cards.append(item[0][0])
    return cards


# ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'J', 'K'] should equal ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

print(sort_cards('Q286JK395A47T'))


