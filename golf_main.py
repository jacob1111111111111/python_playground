import streamlit as st
import random as rd
import golf_classes as gc


cpu = gc.Hand()
player = gc.Hand()
WriteCards = gc.WriteCards()

st.write('''# Golf \n Welcome to golf! In this game, you will be playing against a computer the automatically goes. ''')

WriteCards.player()
WriteCards.cpu()

turn_0 = True
while turn_0:
    card_1 = int(st.text_input("""Your turn! What do you want your first card's index number to be? Please type in 
    an integer from 0-8. """))
    try:
        # make it so I don't have to write gc every time
        player.cards_0or1[card_1 // 3][card_1 % 3] = 1
        player.show_cards()
    except IndexError or ValueError:
        st.write('Sorry, that was an invalid argument. Please try again.')

    card_2 = int(st.text_input("""What do you want your second card's index number to be? Please type in 
    an integer from 0-8. """))
    try:
        player.cards_0or1[card_2 // 3][card_2 % 3] = 1
        player.show_cards()
    except IndexError or ValueError:
        st.write('Sorry, that was an invalid argument. Please try again.')
    turn_0 = False

cpu_turn_0 = True
while cpu_turn_0:
    st.write('The computer is going. These are its cards.')
    for i in range(2):
        card_1 = rd.randint(0, 8)
        cpu.cards[card_1 // 3][card_1 % 3] = card_1
        cpu.cards_0or1[card_1 // 3][card_1 % 3] = 1
    WriteCards.cpu()
    cpu_turn_0 = False
st.write('The computer has successfully gone.')
