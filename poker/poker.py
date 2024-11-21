import random

# Kreuz: ♣
# Pik: ♠
# Herz: ♥
# Karo: ♦

class Card:

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return self.color + ' ' + self.value
    
def create_deck():
    colors = ['♣', '♠', '♥', '♦']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for color in colors:
        for value in values:
            deck.append(Card(value, color))
    return deck

def get_5_cards(deck):
    random.shuffle(deck)
    cards = deck[:5]
    return cards

def calculate_score(cards):
    if is_straight(cards) and is_same_color(cards) and is_highest_cards(cards): # royal flush
        return 10
    if is_straight(cards) and is_same_color(cards): # straight flush
        return 9
    if is_same(cards, 4): # four of a kind
        return 8
    if is_same(cards, 3) and is_same(cards, 2): # full house
        return 7
    if is_same_color(cards): # flush
        return 6
    if is_straight(cards): # straight
        return 5
    if is_same(cards, 3):   # three of a kind
        return 4
    if is_two_pair(cards): # two pair
        return 3
    if is_same(cards, 2):  # pair
        return 2
    return 1

def is_highest_cards(cards):
    values = []
    for card in cards:
        values.append(card.value)
    if 'A' in values and '10' in values:
        return True

def is_same(cards, count):
    values = []
    for card in cards:
        values.append(card.value)
    for value in values:
        if values.count(value) == count:
            return True
    return False

def is_two_pair(cards):
    values = []
    for card in cards:
        values.append(card.value)
    for value in values:
        if values.count(value) == 2:
            values.remove(value)
            break
    for value in values:
        if values.count(value) == 2:
            return True
    return False

def is_straight(cards):
    values = []
    straight1 = True
    straight2 = True
    for card in cards:
        value = card.value
        if value == 'J':
            values.append(11)
                
        elif value == 'Q':
            values.append(12)
                
        elif value == 'K':
            values.append(13)
                
        elif value == 'A':
            values.append(14)
        else:
            values.append(int(value))
    values.sort()
    
    for i in range(len(values)-1):
        if values[i] + 1 != values[i+1]:
            straight1 = False
            break
        
    for value in values:
        if value == 14:
            values.remove(value)
            values.append(1)
    values.sort()
    
    for i in range(len(values)-1):
        if values[i] + 1 != values[i+1]:
            straight2 = False
            break
    return straight1 or straight2

def is_same_color(cards):
    color = cards[0].color
    for card in cards:
        if card.color != color:
            return False
    return True

def print_cards(cards):
    output = ''
    for card in cards:
        output += str(card) + '  '
    print(output)

def main():
    deck = create_deck()
    results = {i : 0 for i in range(1, 11)}
    tries = int(input('How many tries? '))
    for i in range(tries):
        cards = get_5_cards(deck)
        results[calculate_score(cards)] += 1
    
    for key, value in results.items():
        print(f'{key}: {round(value/tries*100, 6)} %')

if __name__ == '__main__':
    main()