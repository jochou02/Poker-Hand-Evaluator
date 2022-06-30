class Card:

    def __init__(self, rank, suit):
        assert isinstance(rank, (str, int)) and isinstance(suit,str)
        self.rank = rank
        self.suit = suit

    def __lt__(self, other_card):
        rank_order = '2345678910JQKA'
        if self.rank == other_card.rank:
            suit_order = 'clubsdiamondsheartsspades'
            return suit_order.find(self.suit) < suit_order.find(other_card.suit)
        return rank_order.find(str(self.rank)) < rank_order.find(str(other_card.rank))

    def __repr__(self) -> str:
        return f'{self.rank} of {self.suit}'

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit


