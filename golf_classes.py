import random as rd
import streamlit as st


class Hand:
    def __init__(self):
        self.cards = [
            [rd.randint(-2, 9), rd.randint(-2, 9), rd.randint(-2, 9)],
            [rd.randint(-2, 9), rd.randint(-2, 9), rd.randint(-2, 9)],
            [rd.randint(-2, 9), rd.randint(-2, 9), rd.randint(-2, 9)]
        ]

        self.cards_0or1 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def show_cards(self):
        for row in range(3):
            cards_list = ''
            for card in range(3):
                if self.cards_0or1[row][card] == 1:
                    cards_list += str(self.cards[row][card]) + ' '
                else:
                    cards_list += '? '
            st.write(cards_list)


cpu = Hand()
player = Hand()


class WriteCards:
    def cpu(self):
        self.col1, self.col2 = st.columns([4, 6])
        with self.col2:
            st.write('CPU cards:')
            cpu.show_cards()

    def player(self):
        self.col1, self.col2 = st.columns([4, 6])
        with self.col1:
            st.write('Your cards:')
            player.show_cards()

