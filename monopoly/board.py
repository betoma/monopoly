from .cards import Deck
from .player import Player
from .property import Property


class Square:
    def __init__(self, index: int):
        self.loc = index

    def __contains__(self, other: Player):
        return other.loc == self.loc

    def on_square(self, player: Player):
        pass


class PropertySquare(Square):
    def __init__(self, index: int, property: Property):
        super().__init__(index)
        self.property = property


class CardSquare(Square):
    def __init__(self, index: int, deck: Deck):
        super().__init__(index)
        self.deck = deck

    def on_square(self, player: Player):
        self.deck.draw_card(player)


class JustParking(Square):
    def __init__(self, index: int, house_rules: bool = False):
        super().__init__(index)
        self.house_rules = house_rules
        if self.house_rules:
            self.cash_pile = 0

    def on_square(self, player: Player):
        if self.house_rules:
            player.earns(self.cash_pile)
            self.cash_pile = 0


class Go(Square):
    def __init__(self, index: int):
        super().__init__(index)


class GoToJail(Square):
    def __init__(self, index: int):
        super().__init__(index)


class Jail(Square):
    def __init__(self, index: int):
        super().__init__(index)
        self.jail = {}
