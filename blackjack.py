class Card:
    def __init__(self):
        self.cards = [(rank, suit) for rank in range(1, 14)
                      for suit in '♤♥♦♧']
        random.shuffle(self.cards)


def deal(self):
    return self.cards.pop()


def points(self, card):
    rank, suit = card
    if rank == 1:
        return (1, 11)
    elif 2 <= rank < 11:
        return (rank, rank)
    else:
        return (10, 10)
