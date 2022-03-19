
from __future__ import print_function, division
import random


class Card:
    """ Represents a standard playing card.
        Attributes:
        suit: integer 0-3
        rank: integer 1-13 """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __eq__(self, other):
        """Checks whether self and other have the same rank and suit.
        returns: boolean """
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        """Compares this card to other, first by suit, then rank.
        returns: boolean """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:
    """ Represents a deck of cards.
        Attributes:
        cards: list of Card objects. """

    def __init__(self):
        """Initializes the Deck with 52 cards. """
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Returns a string representation of the deck. """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck.
        card: Card """
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there.
        card: Card """
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card. """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.
        hand: destination Hand object
        num: integer number of cards to move """
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide the definition of method_name (as a string)
        if it is invoked on obj.
        obj: any python object
        method_name: string method name """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """ Builds a histogram of the suits that appear in the hand.
            Stores the result in attribute suits. """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """ Builds a rank histogram from a hand.
            Stores the result in attribute ranks. """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """ Returns True if the hand has two cards with the same rank, False otherwise. """
        self.rank_hist()
        for val in self.ranks.values():
            if val == 2:
                return True
        return False

    def has_two_pair(self):
        """ Returns True if the hand has two pairs of cards with the same rank, False otherwise. """
        self.rank_hist()
        pairs = 0
        for val in self.ranks.values():
            if val == 2:
                pairs += 1
        return pairs == 2

    def has_three_of_a_kind(self):
        """ Returns True if the hand has three cards with the same rank, False otherwise. """
        self.rank_hist()
        for val in self.ranks.values():
            if val == 3:
                return True
        return False

    def has_straight(self):
        """ Returns True if the hand has five cards with ranks in sequence, False otherwise. """
        self.rank_hist()
        ranks_in_hand = sorted(self.ranks.keys())
        if len(ranks_in_hand) > 4:
            if {1, 10, 11, 12, 13}.issubset(set(ranks_in_hand)):
                return True
            for i in range(len(ranks_in_hand) - 4):
                if ranks_in_hand[i: i + 5][-1] - ranks_in_hand[i: i + 5][0] == 4:
                    return True
        return False

    def has_flush(self):
        """ Returns True if the hand has five cards with the same suit, False otherwise.
            Note that this works correctly for hands with more than 5 cards. """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print('---------------------------')
        print(f'       Pair?: {hand.has_pair()}')
        print(f'     2-Pair?: {hand.has_two_pair()}')
        print(f'3-of-a-kind?: {hand.has_three_of_a_kind()}')
        print(f'      Flush?: {hand.has_flush()}')
        print(f'   Straight?: {hand.has_straight()}')
        print('')
