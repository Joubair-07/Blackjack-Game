"""Blackjack, by Alpha Joubair alphajoubair04@gmail.com
This game is also known as 21."""

# Using both random (to generate a random ) and sys to exit 
# game if needed.
import random, sys

# Set up constants:
HEART = chr(9829) # For '♥'
CLUBS = chr(9827) # For '♣'
SPADS = chr(9824) # For '♠'
DIAMONDS = chr(9830) # For '♦'


def main():
    print("""Blackjack, by Alpha Joubair alphajoubair04@gmail.com

    Ruels:
      Try to get as close to 21 without goung over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your firs play, u can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.""")





# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()