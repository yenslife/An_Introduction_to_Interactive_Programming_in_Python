# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48) card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    
# initialize some useful global variables
in_play = False
outcome = ""
choice_text = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    # card back
    def draw_card_back(self, canvas, pos):
        # red back
        card_loc = (CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0], CARD_BACK_CENTER[1])
        # blue back
        # card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        # draw card back
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        pass	# create Hand object

    def __str__(self):
        out_str = "Hand contains "
        for card in self.cards:
            out_str += str(card) + " "
        return out_str
        pass	# return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)
        pass	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        ace_count = 0
        for card in self.cards:            
            if card.get_rank() != 'A':
                #print "has A"
                value += VALUES[card.get_rank()]
            else:
                ace_count += 1
        # add Ace   
        while ace_count > 0:
            ace_count -= 1
            if value + 11 > 21:
                value += 1
            else:
                value += 11
                    
        #debug
        #print value
        return value
        pass	# compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        i = 0
        for card in self.cards:
            card.draw(canvas, (pos[0] + i * CARD_SIZE[0] + i * 20, pos[1]))
            i += 1
        
        pass	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.card_list = []
        for i in SUITS:
            for j in RANKS:
                card = Card(i, j)
                self.card_list.append(card)
                
        pass	# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.card_list)
        pass    # use random.shuffle()

    def deal_card(self):
        card = self.card_list.pop()
        return card
        pass	# deal a card object from the deck
    
    def __str__(self):
        out_str = "Deck contains "
        for card in self.card_list:
            out_str += str(card) + " "
        return out_str
        pass	# return a string representing the deck



#define event handlers for buttons
def deal():
    
    global outcome, in_play, choice_text, score

    # your code goes here
    global game_deck, player_hand, dealer_hand
    game_deck = Deck()
    game_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(game_deck.deal_card())
    player_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    dealer_hand.add_card(game_deck.deal_card())
    outcome = ""
    choice_text = "Hit or stand??"
    
    if in_play == True:
        outcome = "You lost the round :( "
        score -= 1
    
    in_play = True
    
    # debug
    #print_value()
    
def hit():
    #pass	# replace with your code below
    
    global in_play, score, outcome, choice_text
 
    # if the hand is in play, hit the player
    if in_play and player_hand.get_value() <= 21:
        player_hand.add_card(game_deck.deal_card())
        outcome = ""
   
    # if busted, assign a message to outcome, update in_play and
