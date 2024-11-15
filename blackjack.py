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

BACKSIDE = 'backside'


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
    # Set up money
    money = 50000
    while True: # Main game loop
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()

        # Let the player to enter their bet for this round:
        print('Money: ', money)
        bet = getBet(money)

        # Give the dealer and the player two cards from the ceck each:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions:
        print('Bet: ', bet)
        while True: # Keep looping until the player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has bust:
            if getHandValue(playerHand) > 21:
                break
            
            # Get the player's move, ether H, S, or D:
            move = getMove(playerHand, money - bet)

            # Gandle the player actions :
            if move == 'D':
                # Player is doublig down, they can increase their bet:
                additionalBet = getBet(min(bet,  (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet : ', bet)

            if move in ('H', 'D'):
                # Hit/doubling down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The player has busted:
                    continue
              
            if move in ('S', 'D'):
                # Stand/doubling down stops the plyers's turn.
                break
            
        # Handle the dealer's actionsl:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits:
                print('Dealer hits...')
                dealerHand.append((deck.pop()))
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break # The dealer has busted
                input('press Enter to continue...')
                print('\n\n')

        # Show the final hands:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Handle whether the player won, lost or tied:
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you')

        input('press Enter to continue...')
        print('\n\n')






def getBet(maxBet):
    """Ask the player how much they want to bet for this round."""
    while True: # Keep asking until they enter a valid amount.
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Tanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue # If the player didn't enter a nuber, ask again.
        
        bet = int(bet)
        if 1 <= bet <= maxBet :
            return bet # Player entered a valid bet.
        

def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEART, DIAMONDS, SPADS, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add the numberd cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # Add the face and ace cards

    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first
    card if showDealerHand is False."""
    # empty line
    if showDealerHand:
        print('DEALER: ', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        displayCards([BACKSIDE] + dealerHand[1:])

    # Show the player's cards:
    print('PLAYER: ', getHandValue(playerHand))
    displayCards(playerHand)



def getHandValue(cards):
    """Reruens the value of the cards . Face cards are worth 10, aces are worth 
    11 or 1 (this function picks the most suitable ace Value)."""
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0] # Card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10 # Face cards are woth 10 points.
        else: 
            value += int(rank) # Numbered cards are with their number.
    
    # Add the value for the aces:
    for i in range(numberOfAces):
        # if another 11 can be added without busting, do so:
        if value + 11 <= 21:
            value += 11
        else:
            value += 1

    return value
        

def displayCards(cards):
    """Display all the cards in the cards list."""
    rows = [''] * 4  # The text to display on each row.

    for  card in cards:
        rows[0] += ' ___  ' # Print the top line of the card.
        if card == BACKSIDE:
            # P rint a card's back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '

        else :
            # Print the card's front:
            rank, suit = card # The card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each tow in the screen:
    for row in rows:
        print(row)


def getMove(playerHand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for 
    stand, and 'D' for double down."""
    while True: # Keep looping until the player enters a correct move.
        # Determine what moves the player can make :
        moves = ['(H)it', '(S)tand']

        # The player can double down on their first move, whick we can
        # tell because they'll have exactly two cards:
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move :
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move  # Player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move  # Player has entered a valid move.

        

        
            







# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()