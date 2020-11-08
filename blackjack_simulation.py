
from random import shuffle

# DON'T CHANGE OR REMOVE THESE LISTS
# The first is a list of all possible card ranks: 2-10, Jack, King, Queen, Ace
# The second is a list of all posible card suits: Hearts, Diamonds, Clubs, Spades
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["H", "D", "C", "S"]

# This class represents an individual playing card
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # DON'T CHANGE OR REMOVE THIS
    # This function creates a string out of a Card for easy printing.
    def __str__(self):
        return "[" + self.suit + ", " + self.rank + "]"

# This class represents a deck of playing cards
class Deck():
    def __init__(self):
        self.cards = []

        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r))
    
        
    # DON'T CHANGE OR REMOVE THIS
    # This function will shuffle the deck, randomizing the order of the cards
    # inside the deck.
    # It takes an integer argument, which determine how many times the deck is
    # shuffled.
    def shuffle_deck(self, n = 5):
        for i in range(n):
            shuffle(self.cards)

    # This function will deal a card from the deck. The card should be removed
    # from the deck and added to the player's hand.
    def deal_card(self, player):
        player.hand.append(self.cards.pop())
    

    # DON"T CHANGE OR REMOVE THIS
    # This function constructs a string out of a Deck for easy printing.
    def __str__(self):
        res = "[" + str(self.cards[0])
        for i in range(1, len(self.cards)):
            res += ", " + str(self.cards[i])
        res += "]"
        return res

# This class represents a player in a game of Blackjack
class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.status = True 

    def value(self):
        playerValue = 0
        for i in self.hand:
                if i.rank == "J" or i.rank == "Q" or i.rank == "K":
                    playerValue += 10
                elif i.rank == "A":
                    if playerValue >= 11:
                        playerValue += 1
                    else:
                        playerValue += 11
                else:
                    playerValue += int(i.rank)

        return playerValue 
            
            

    def choose_play(self):
        #playerStatus = "";
        if self.value() < 17:
            self.status = True
            playerStatus = "Hit"
        else:
            self.status = False
            playerStatus = "Stay"

        return playerStatus 
        

    # DON'T CHANGE OR REMOVE THIS
    # This function creates a string representing a player for easy printing.
    def __str__(self):
        res = "Player: " + self.name + "\n"
        res += "\tHand: " + str(self.hand[0])
        for i in range(1, len(self.hand)):
            res += ", " + str(self.hand[i])
        res += "\n"
        res += "\tValue: " + str(self.value())
        return res

# This class represents a game of Blackjack
class Blackjack():
    def __init__(self, players):
        self.players = players
        self.deck = Deck()

        self.deck.shuffle_deck()
        for i in self.players:
            self.deck.deal_card(i)
            self.deck.deal_card(i)
        pass

    def play_game(self):
        loop = True
        while loop == True:
            for i in self.players:
                if i.status == True:
                    if i.choose_play() == "Hit":
                        self.deck.deal_card(i)
                        if i.value() > 21:
                            print(i.name + " has busted!")
                            i.status = False
                    elif i.choose_play() == "Stay":
                        pass

            count = 0
            for j in self.players:
                if i.status == False:
                    count+=1

            if (count == len(self.players)):
                loop = False

        #winner and tie loop
        highestHand = []
        for h in self.players:
                if h.value() <= 21:
                    highestHand.append(h.value())

    
        count = 0
        for w in self.players:
            if w.value() <= 21:
                if not w.value() < max(highestHand):
                    count+=1
                    name = w.name

        if count == 1:
            print("The winner is " + name + ".")
        else:
            print("There is a tie.")

        #tie loop
        tie = []
        for t in self.players:
            tie.append(t.value())

        count = 0
        for d in self.players:
            if d.value() == tie[0]:
                count += 1

        if count == len(self.players):
            print("There was a tie.")
        

        #no winner loop
        count = 0
        for f in self.players:
            if f.value() > 21:
                count += 1

        if (count == len(self.players)):
            print("There is no winner.")

        pass
                
                

    # DON'T CHANGE OR REMOVE THIS
    # This function creates a string representing the state of a Blackjack game
    # for easy printing.
    def __str__(self):
        res = "Current Deck:\n\t" + str(self.deck)
        res = "\n"
        for p in self.players:
            res += str(p)
            res += "\n"
        return res

# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    # Uncomment each section of test code as you finish implementing each class
    # for this problem. Uncomment means remove the '#' at the front of the line
    # of code.
    
    # Test Code for your Card class
    c1 = Card("H", "10")
    c2 = Card("C", "A")
    c3 = Card("D", "7")

    print(c1)
    print(c2)
    print(c3)

    print()

    # Test Code for your Deck class
    d1 = Deck()
    d1.shuffle_deck(10)
    print(d1)

    print()

    # Test Code for your Player class
    p1 = Player("Alice")
    p2 = Player("Bob")
    d1.deal_card(p1)
    d1.deal_card(p2)
    print(p1.value())
    print(p2.value())
    d1.deal_card(p1)
    d1.deal_card(p2)
    print(p1.value())
    print(p2.value())
    d1.deal_card(p1)
    d1.deal_card(p2)
    print(p1.value())
    print(p2.value())
    print(p1)
    print(p2)
    print(p1.choose_play())
    print(p2.choose_play())

    print()

    # Test Code for your Blackjack class
    players = [Player("Summer"), Player("Rick"), Player("Morty"), Player("Jerry")]
    game = Blackjack(players)
    print(game)
    game.play_game()
    print(game)



