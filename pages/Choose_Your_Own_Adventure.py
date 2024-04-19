import streamlit as st
from story_content import story

# Initialize session state for story part if it doesn't exist
if 'current_part' not in st.session_state:
    st.session_state.current_part = 'start'

# Function to display a story part and choices
def show_story_part(part_key):
    st.session_state.current_part = part_key  # Update the current part in session state
    st.write(story[part_key]["text"])
    for option_text, next_part in story[part_key]["choices"]:
        if st.button(option_text):
            show_story_part(next_part)

# Set up the main page
st.header("Choose Your Own Adventure")
show_story_part(st.session_state.current_part)
