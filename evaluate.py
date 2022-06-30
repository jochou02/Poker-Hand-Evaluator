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

        if r in ranks['Singles']:
            ranks['Doubles'].append(ranks['Singles'].pop())
        elif r in ranks['Doubles']:
            ranks['Triples'].append(ranks['Doubles'].pop())
        elif r in ranks['Triples']:
            ranks['Quads'].append(ranks['Triples'].pop())
        else:
            ranks['Singles'].append(r)

        suits[s].append(r)
        
    # One pair
    if len(ranks['Doubles']) == 1:
        hand_rankings[9] = True
    # Two pair
    elif len(ranks['Doubles']) > 1:
        hand_rankings[8] = True
    # Three of a kind
    if len(ranks['Triples']) > 0:
        hand_rankings[7] = True
    # TODO: Straight
    if rank_order.find(ranks[4]) - rank_order.find(ranks[0]) == 4:
        hand_rankings[6] = 1
    # Flush
    if max([len(i) for i in suits.values()]) >= 5:
        hand_rankings[5] = True
    # TODO: Full House
    
    # Quads
    if len(ranks['Quads']) > 0:
        hand_rankings[3] = True
    # Straight flush
    if hand_rankings[6] and hand_rankings[5]:
        hand_rankings[2] = True
    # TODO: Royal flush
    if hand_rankings[2] and ranks[4] == 'K':
        hand_rankings[1] = True


    for i in hand_rankings.items():
        if i[1] == 1:
            return i[0]

    
card1 = Card("A", "Spades")
card2 = Card("K", "Diamonds")
card3 = Card("Q", "Spades")
card4 = Card("J", "Spades")
card5 = Card("T", "Spades")

print(evaluate([card1, card2, card3, card4, card5]))
