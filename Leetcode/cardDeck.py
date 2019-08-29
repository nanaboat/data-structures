from random import randint

class CardDeck:
    def __init__(self):
        self.cards = {1:'Spades', 2: 'Hearts', 3: 'Club', 4: 'Diamonds', 5: 'Joker'}
        self.card_vals = {11: 'Jack', 12: 'Queen', 13: 'King'}

class CardGame:
    def __init__(self, size=2**32):
        self.deck = None
        self.deck_size = size

    def start(self):
        print("Welcome!!!")
        self.deck = CardDeck()
    
    def _get_random(self, a =0, b=None):
        if not b:
            b = self.deck_size
        return randint(a, b)
    
    def shuffle(self):
        x = self._get_random()
        count = 0
        results = []
        while count < x:
            count += 1
            results.append((self._get_random(1, 13), self._get_random(1, 5)))
        return self.display(results)

    def display(self, results):
        print("You have {0} random cards\n".format(len(results)))
        for k, v in results:
            card = self.deck.cards[v]
            if card == 'Joker':
                print("You have a {0} card".format(card))
            else:
                if k > 10:
                    k = self.deck.card_vals[k]
                print("You have {0} {1} card".format(k, card))
        print() 
    
    def end(self):
        print("Game ended")

if __name__ == "__main__":
    game = CardGame(52)
    game.start()
    game.shuffle()
    game.end()

