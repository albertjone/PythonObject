class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.hard,self.soft = self._points()

class NumberCard(Card):
    def _points(self):
        return int(self.rank),int(self.suit)

class AceCard(Card):
    def _points(self):
        return 1,11

class FaceCard(Card):
    def _points(self):
        return 10,10

cards = [AceCard('A','11'),NumberCard('2','11'),NumberCard('3','11')]

class Suit:
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol

Club,Diamond,Heart,Spade = Suit('Club','14'),Suit('Diamond','13'),Suit('Heart','12'),Suit('Spade','11')

cards = [AceCard('A',Spade),NumberCard('2',Spade),NumberCard('3',Spade)]

def card(rank,suit):
    if rank ==1 : return AceCard('A',suit)
    elif 1 < rank <11 : return NumberCard(str(rank),suit)
    elif 11 <= rank <14:
        name = {11:'J',12:'Q','13':'K'}[rank]
        return FaceCard(name,suit)
    else:
        raise Exception("Rank out of Range")

deck = [card(rank,suit)
        for rank in range(1,14)
            for suit in [Club,Diamond,Heart,Spade]]
print(deck)



def card4(rank,suit):
    class_ = {1:AceCard,11:FaceCard,12:FaceCard,13:FaceCard}.get(rank,NumberCard)
    return class_(rank,suit)
