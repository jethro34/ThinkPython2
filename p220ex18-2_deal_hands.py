# Write a Deck method called deal_hands that takes two parameters:
# the number of hands and the number of cards per hand.
# It should create the appropriate number of Hand objects,
# deal the appropriate number of cards per hand, and return a list of Hands.


import random


class Card:
    """ Represents a standard playing card. """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    """ Represents a standard 52-card deck. """

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_hands, num_cards):
        hands_list = []
        for i in range(num_hands):
            hand = Hand(str(i + 1))
            self.move_cards(hand, num_cards)
            hands_list.append(hand)
        return hands_list


class Hand(Deck):
    """ Represents a hand of playing cards. """

    def __init__(self, label=''):
        self.cards = []
        self.label = label


deck = Deck()
# hand = Hand('new hand')
# deck.move_cards(hand, 5)
# print(hand)
print(deck.deal_hands(5, 5))
for hand in deck.deal_hands(5, 5):
    for card in hand.cards:
        print(card)
    print('____________________')