import random

# Class used to create player's objects. Name and player's cards.
class Player:
    def __init__(self, name):
        self.name = name
        self.player_cards = []

# Class responsible for creating a deck of cards.
class Deck:
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits
        self.cards = [(rank, suit) for rank in self.ranks for suit in self.suits]
        # It shuffles the cards to randomize the order.
        random.shuffle(self.cards)

#  Main Class for the War card game. In its constructor, it sets up the initial game state. 
class WarGame:
    def __init__(self):

        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # Card Ranking
        self.suits = ["clubs", "diamonds", "spades", "hearts"]  # Card Suits
        self.deck = Deck(self.ranks, self.suits)  # Create a Deck object and shuffle it


    # Method responsible for distributing the shuffled deck to the two players.
    def deal_cards(self):
        self.player1.player_cards = self.deck.cards[:26]
        self.player2.player_cards = self.deck.cards[26:]

        return self.player1.player_cards, self.player2.player_cards

    # Method compares two cards based on their ranks and returns the result
    def compare_cards(self, card1, card2):
        rank1 = self.ranks.index(card1[0])
        rank2 = self.ranks.index(card2[0])
        
        if rank1 > rank2:
            return 1  # Player1 wins
        elif rank1 < rank2:
            return 2  # Player2 wins
        else:
            return 0  # It's a tie


    def start_game(self):
        print("Welcome to the War Game!")
        # Asking for the Player's 1 name
        player1_name = input("Enter Your name: ")
        self.player1 = Player(player1_name)
        # Creating a Player 2 object for the computer and assigns the name "Computer"
        self.player2 = Player("Computer")

        # Setting up the initial decks of cards for both players by calling the deal_cards method
        player1_deck, player2_deck = self.deal_cards()

        self.round = 0 # Initializing round 0

        # The game continues while both player1_deck and player2_deck are not left empty
        while player1_deck and player2_deck:
            self.round += 1
            user_input = input(f"Round {self.round}: Press Enter to start or 'q' to quit.").strip()
            if user_input.lower() == 'q':
                print("Game quit by the player.")
                break

            # Player1 always starts, player2 is always a computer
            player1_card = self.player1.player_cards.pop(0)
            player2_card = self.player2.player_cards.pop(0)
            print(f"{self.player1.name} drew {player1_card[0]} of {player1_card[1]}.")

            print(f"{self.player2.name} drew {player2_card[0]} of {player2_card[1]}.")

            

if __name__ == '__main__':
    game = WarGame()
    game.start_game()





