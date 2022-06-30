# File to test functionalty #

from card import Card
from evaluate import evaluate

ranks = '23456789TJQKA'
suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

def test(expected, actual, test_number):
    if(actual == expected):
        print(f'{test_number} PASSED')
    else:
        print(f'{test_number} FAILED Actual: {actual} Expected: {expected}')

# Populate a deck with Cards
# 0 - 3: Rank 2
# 4 - 7: Rank 3
# ...
# 44 - 47: Rank K
# 48 - 51: Rank A
deck = [Card(rank, suit) for rank in ranks for suit in suits]

# 1: Royal flush

expected = (1, 'Royal Flush')
actual = evaluate([deck[49], deck[45], deck[41], deck[37], deck[33], deck[5], deck[1], deck[25]])
test(expected, actual, 1.1)

# 2: Straight flush

expected = (2, 'K High Straight Flush')
actual = evaluate([deck[37], deck[33], deck[32], deck[41], deck[29], deck[47], deck[45]])
test(expected, actual, 2.1)

# 3: Four of a kind

expected = (3, 'Quad: 2s')
actual = evaluate([deck[1], deck[0], deck[2], deck[50], deck[3]])
test(expected, actual, 3.1)

# 4: Full House

expected = (4, 'Full House: 5 Full of A')
actual = evaluate([deck[13], deck[50], deck[15], deck[23], deck[14], deck[49]])
test(expected, actual, 4.1)

expected = (4, 'Full House: A Full of 5')
actual = evaluate([deck[13], deck[50], deck[15], deck[48], deck[14], deck[49]])
test(expected, actual, 4.2)

# 5: Flush

expected = (5, 'T High Flush')
actual = evaluate([deck[0], deck[4], deck[8], deck[12], deck[17], deck[32]])
test(expected, actual, 5.1)

# 6: Straight

expected = (6, 'K High Straight')
actual = evaluate([deck[37], deck[34], deck[32], deck[41], deck[29], deck[47], deck[45]])
test(expected, actual, 6.1)

# 7: Three of a Kind

expected = (7, 'Three of a Kind: 7s')
actual = evaluate([deck[20], deck[11], deck[22], deck[37], deck[21]])
test(expected, actual, 7.1)

# 8: Two Pair

expected = (8, 'Two Pair: 4s and 7s')
actual = evaluate([deck[20], deck[11], deck[51], deck[10], deck[21]])
test(expected, actual, 8.1)

# 9: One Pair

expected = (9, 'One Pair: 2s')
actual = evaluate([deck[0], deck[6], deck[22], deck[40], deck[1]])
test(expected, actual, 9.1)

# 10: High Card

expected = (10, 'K High')
actual = evaluate([deck[1], deck[5], deck[9], deck[13], deck[44]])
test(expected, actual, 10.1)
 


