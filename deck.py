from card import Card
from random import shuffle

class Deck(object):
    def __init__(self):
        self.cards = []
        def createCards():
            ranks = [2,3,4,5,6,7,8,9,10,'A', 'J', 'Q', 'K']
            suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
            count = 1
            for suit in suits:
                for rank in ranks:
                    if rank == 'A':
                        count = 11
                        self.cards.append(Card(suit,rank,count))
                    else:
                        if count < 10:
                            count += 1
                            self.cards.append(Card(suit,rank,count))
                        else:
                            count = 10
                            self.cards.append(Card(suit,rank,count))
                count = 1
        createCards()
        shuffle(self.cards)

    def showCards(self):
        for card in self.cards:
            print card.suit, card.rank
        return self



#deck.showCards()
