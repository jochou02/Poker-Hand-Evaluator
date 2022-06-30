# File to test functionalty #

from card import Card
from evaluate import evaluate

# 1: Royal flush
# 2: Straight flush
# 3: Four of a kind
# 4: Full House
# 5: Flush
# 6: Straight
# 7: Three of a Kind
# 8: Two Pair
# 9: One Pair
# 10: High Card

card1 = Card("J", "Clubs")
card2 = Card("T", "Clubs")
card3 = Card("K", "Clubs")
card4 = Card("Q", "Clubs")
card5 = Card("A", "Clubs")

print('Expected: Royal Flush')
print(f'Got: {evaluate([card1, card2, card3, card4, card5])}') 

card1 = Card("J", "Clubs")
card2 = Card("T", "Clubs")
card3 = Card("K", "Clubs")
card4 = Card("Q", "Clubs")
card5 = Card("9", "Clubs")

print('Expected: K High Straight Flush')
print(f'Got: {evaluate([card1, card2, card3, card4, card5])}') 


