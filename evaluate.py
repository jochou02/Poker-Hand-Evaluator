from enum import unique
from card import Card

def evaluate(list_of_cards):
    
    rank_order = '23456789TJQKA'

    hand_rankings = {
        1: False, # Royal flush
        2: False, # Straight flush
        3: False, # Four of a kind
        4: False, # Full House
        5: False, # Flush
        6: False, # Straight
        7: False, # Three of a Kind
        8: False, # Two Pair
        9: False, # One Pair
        10: True # High Card
    }

    ranks = {
        'Singles': [],
        'Doubles': [],
        'Triples': [],
        'Quads': []
    }

    # Extract ranks, without duplicates
    rank_only = []

    suits = {
        'Diamonds': [],
        'Clubs': [],
        'Hearts': [],
        'Spades': []
    }

    list_of_cards.sort()
    for card in list_of_cards:
        r = card.get_rank()
        s = card.get_suit()

        if r not in rank_only:
            rank_only.append(r)

        if r in ranks['Singles']:
            ranks['Doubles'].append(ranks['Singles'].pop())
        elif r in ranks['Doubles']:
            ranks['Triples'].append(ranks['Doubles'].pop())
        elif r in ranks['Triples']:
            ranks['Quads'].append(ranks['Triples'].pop())
        else:
            ranks['Singles'].append(r)

        suits[s].append(r)
        
    output = tuple()

    # High Card
    output = (10, f'{rank_only[-1]} High')
    # One pair
    if len(ranks['Doubles']) > 0:
        hand_rankings[9] = True
        output = (9, f'One Pair: {ranks["Doubles"][0]}s')
    # Two pair
    if len(ranks['Doubles']) > 1:
        hand_rankings[8] = True
        output = (8, f'Two Pair: {ranks["Doubles"][-2]}s and {ranks["Doubles"][-1]}s')
    # Three of a kind
    if len(ranks['Triples']) > 0:
        hand_rankings[7] = True
        output = (7, f'Three of a Kind: {ranks["Triples"][-1]}s')
    # Straight
    for i in range(len(rank_only) - 4):
        pos = rank_order.find(rank_only[i])
        if rank_order.find(rank_only[i + 1]) == pos + 1 and \
            rank_order.find(rank_only[i + 2]) == pos + 2 and \
            rank_order.find(rank_only[i + 3]) == pos + 3 and \
            rank_order.find(rank_only[i + 4]) == pos + 4:
            hand_rankings[6] = True
            output = (6, f'{rank_only[i + 4]} High Straight')
            straight_msg = output[1]
    # Flush
    if max([len(i) for i in suits.values()]) >= 5:
        hand_rankings[5] = True
        for pair in suits.items():
            if len(pair[1]) >= 5:
                output = (5, f'{pair[1][-1]} High Flush')
    # Full House
    if (hand_rankings[7] and hand_rankings[9]):
        hand_rankings[4] = True
        output = (4, f'Full House: {ranks["Triples"][-1]} Full of {ranks["Doubles"][-1]}')
    if len(ranks['Triples']) > 1:
        hand_rankings[4] = True
        output = (4, f'Full House: {ranks["Triples"][-1]} Full of {ranks["Triples"][-2]}')
    # Quads
    if len(ranks['Quads']) > 0:
        hand_rankings[3] = True
        output = (3, f'Quad: {ranks["Quads"][-1]}s')
    # Straight flush
    if hand_rankings[6] and hand_rankings[5]:
        hand_rankings[2] = True
        output = (2, straight_msg + ' Flush')
    # Royal flush
    if hand_rankings[2] and 'A' in rank_only and 'T' in rank_only:
        if rank_order.find('T') + 4 == rank_order.find('A'):
            hand_rankings[1] = True
            output = (1, f'Royal Flush')

    # Return best hand
    return output
