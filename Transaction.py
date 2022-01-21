import streamlit as st
import random as r

player_cards = [
    [r.randint(-2, 9), r.randint(-2, 9), r.randint(-2, 9)],
    [r.randint(-2, 9), r.randint(-2, 9), r.randint(-2, 9)],
    [r.randint(-2, 9), r.randint(-2, 9), r.randint(-2, 9)]
]
player_cards_0or1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
cpu_cards = [
    [r.randint(-2, 9), r.randint(-2, 9), r.randint(-2, 9)],
    [r.randint(-2, 9), r.randint(-2, 9), r.randint(-2, 9)],
    [r.randint(-2, 9), r.randint(-2, 9), r.randint(-2, 9)]
]
cpu_cards_0or1 = player_cards_0or1


def show_cards():
    for row in range(3):
        cards_list = ''
        for card in range(3):
            if player_cards_0or1[row][card] == 1:
                cards_list += str(player_cards[row][card])
            else:
                cards_list += '? '
        st.write(cards_list)


def show_cpu_cards():
    for row in range(3):
        cards_list = ''
        for card in range(3):
            if cpu_cards_0or1[row][card] == 1:
                cards_list += str(cpu_cards[row][card])
            else:
                cards_list += '? '
        st.write(cards_list)


class Hand:

    def __init__(self):


        #add self statement
        self.cards = [
            [r.randint(-2, 9), r.randint(-2, 9), r.randint(-2, 9)],
            [r.randint(-2, 9), r.randint(-2, 9), r.randint(-2, 9)],
            [r.randint(-2, 9), r.randint(-2, 9), r.randint(-2, 9)]
        ]

        self.cards_0or1 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def show_cards_class(self):
        for row in range(3):
            cards_list = ''
            for card in range(3):
                if cards_0or1[row][card] == 1:
                    cards_list += str(cards[row][card])
                else:
                    cards_list += '? '
            st.write(cards_list)


st.write('''
# Golf

Welcome to golf! In this game, you will be playing against a computer the automatically goes. 
''')

col1, col2 = st.columns([4, 6])

with col1:
    st.write('CPU cards:')
    show_cpu_cards()
with col2:
    st.write('Your cards:')
    show_cards()

first_card = int(st.text_input("""Your turn! What do you want your first card's index number to be? Please type in an 
integer from 0-8. """))
first_turn = True
while first_turn:
    try:
        player_cards_0or1[first_card // 3][first_card % 3] = 1
        show_cards()
    except IndexError or ValueError:
        st.write('Sorry, that was an invalid argument. Please try again.')
    first_turn = False


