# blackjack-simulation
Homework for IAE 101 (SBU)

I used classes and functions to simulate a simplified game of Blackjack (21). The game begins with a standard deck of 52 playing cards (no jokers). Each player is dealt two cards to start with. The winner of a hand of Blackjack is the player whose hand has the highest value without going over 21.

When calculating the value of a hand, add up the rank of each card in the player's hand, where the numbered cards have ranks 2 through 10. The face cards, Jack, King, and Queen, each add 10 to the value of a player's hand. The Ace card can be treated as adding either 1 or 11 to the value of the player's hand, depending upon which brings the player closer to winning.

Player's may request additional cards (a "hit") in order to bring the value of their hand closer to 21. However, if the value of a player's hand rises above 21, then the player has "busted" and they automatically lose the game.

In this simulation we are ignoring the distinction between player and dealer. We are also ignoring betting, and so all the more sophisticated player actions (such as "splitting") are also being ignored. The behavior of player's is going to be fixed by a simple algorithm.

The program will consist of 4 classes: Card, Deck, Player, Blackjack. Each class represents objects that are elements of a simulated game of Blackjack. 
