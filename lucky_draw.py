import streamlit as st
import random

# Initialize session state
if 'orange_ball_location' not in st.session_state:
    st.session_state.orange_ball_location = random.randint(1, 30)
    st.session_state.choices = []
    st.session_state.trials = 0
    st.session_state.won = False
    st.session_state.current_box = None

st.title("Lucky Draw")
st.write("In this lucky draw, you will win a jackpot if you get an orange ball.")
st.write("There are 6 boxes in front of you, with 5 balls in each box. Among these 30 balls, there is only 1 orange ball (the target) and the other 29 balls are white.")
st.write("When the game begins, you will draw one ball from one of the boxes. Then, you will be told what you get.")
st.write("If you get the orange ball, you win! And the game will stop.")
st.write("If you get a white ball, you can draw again. In total, you have 7 trials to draw a ball.")

# Enlarge the instructional text
st.markdown('<p style="font-size:20px;">Please select your Box and press <strong>Draw Ball</strong></p>', unsafe_allow_html=True)

# Display the 6 boxes as buttons
cols = st.columns(6)
for i, col in enumerate(cols):
    if col.button(f"Box {i+1}"):
        st.session_state.current_box = i + 1

if st.session_state.current_box is not None:
    st.write(f"You selected Box {st.session_state.current_box}")

if st.session_state.trials < 7 and not st.session_state.won and st.session_state.current_box is not None:
    if st.button("Draw Ball"):
        st.session_state.trials += 1
        box_choice = st.session_state.current_box
        ball_number = (box_choice - 1) * 5 + random.randint(1, 5)
        st.session_state.choices.append(box_choice)

        if ball_number == st.session_state.orange_ball_location:
            st.success("Congratulations! You drew the orange ball and won!")
            st.session_state.won = True
        else:
            st.info("You drew a white ball. Try again.")
        st.session_state.current_box = None  # Reset current box after drawing

if st.session_state.trials == 7 and not st.session_state.won:
    st.warning("You've used all 7 trials without drawing the orange ball. Better luck next time!")

if st.session_state.trials > 0:
    st.write("### Game Summary")
    st.write(f"Boxes chosen over the trials: {st.session_state.choices}")
    if st.session_state.won:
        st.write(f"The orange ball was in box number {((st.session_state.orange_ball_location - 1) // 5) + 1}.")
    else:
        st.write(f"The orange ball was located in box number {((st.session_state.orange_ball_location - 1) // 5) + 1}.")

# Placeholder for the restart button
restart_placeholder = st.empty()

# Button to restart the game
with restart_placeholder:
    if st.button("Restart Game"):
        st.session_state.orange_ball_location = random.randint(1, 30)
        st.session_state.choices = []
        st.session_state.trials = 0
        st.session_state.won = False
        st.session_state.current_box = None
        st.experimental_rerun()