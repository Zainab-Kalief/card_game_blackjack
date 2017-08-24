from random import shuffle
from card import Card
from deck import Deck
from player import Player

class Dealer(object):
    def __init__(self):
        self.name = 'Trump'
        self.hand = []
        self.points = 0
        self.players = []

    def currentPlayers(self, *players):
        self.players.extend(players)
        self.players.append(self)
        return self

    def dealHand(self,deck):
        start = 0
        end = 2
        for player in self.players:
            player.hand.extend(deck.cards[start:end])
            start += 2
            end += 2
        del deck.cards[:start]
        return self

    def findWinner(self):
        cardCount = {}
        maxCard = 0
        winner = ''
        x = 0
        while x < 3:

            for player in self.players: #calculate everyone's card value
                cardVal = 0
                for card in player.hand:
                    cardVal += card.value
                cardCount[player.name] = cardVal
            print cardCount
            for key in cardCount: #find the max card value and winner
                if cardCount > 21: #if you have higher than 21 you forfiete all cards
                    for player in self.players:
                        if key == player.name:
                            player.hand = []
                if cardCount[key] > maxCard and cardCount[key] <= 21:
                    maxCard = cardCount[key]
                    winner = key
                if maxCard == 21:
                    winner = key
            for player in self.players: #award the winner with 10 points
                if player.name == winner:
                    print winner, 'won this with', maxCard, '~~', player.hand 
                    for card in player.hand:
                        print winner, 'played', card.rank, 'of', card.suit, '\n'

                    player.points += 10
                if maxCard == 21:
                    player.hand = []
            for player in self.players: #deal out one card to everyone
                player.hand.append(deck.cards.pop())

            x += 1

        return self

deck = Deck()
ply1 = Player('Wura')
ply2 = Player('Nessa')
ply3 = Player('Kunmi')
ply4 = Player('Tiwa')

dealer = Dealer()
dealer.currentPlayers(ply1,ply2,ply3,ply4).dealHand(deck).findWinner()
