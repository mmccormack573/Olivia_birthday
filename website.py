import streamlit as st
import time

st.set_page_config(page_title="Birthday Puzzle", page_icon="🎂")

# Initialize session state stage
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# Safe stage advancement function
def go_to_stage(stage_number):
    st.session_state.stage = stage_number

# Create a container slot that we can wipe clean at the end
header_slot = st.empty()

# Only show the main birthday intro if NOT on the final stage
if st.session_state.stage < 6:
    with header_slot.container():
        st.title("🎂 Happy Birthday!")
        st.write("All answers must be in numbers. If you get stuck, ask me for hints. Good luck!")
else:
    # Clear the placeholder entirely for the grand finale
    header_slot.empty()




#part 1
if st.session_state.stage == 1:
    st.header("Part 1:")
    st.write("Hint: Think of your favorite pet...")
    k = st.number_input("Enter the key:", value=0, step=1, key="input_level_1")
    
    if st.button("Submit Key", key="btn_1"):
        if k == 76:
            st.success("Good job!")
            st.button("Proceed to Part 2", on_click=go_to_stage, args=(2,))
        else:
            st.error("Nope.")




#part 2
elif st.session_state.stage == 2:

    st.header("Part 2:")
    st.info("Using the previous key: Rfc lcvr ajsc gq: msp dgpqr bylac qmle")
    wowy = st.number_input("Enter code:", value=0, step=1, key="input_level_2")
    
    if st.button("Unlock", key="btn_2"):
        if wowy == 456:
            st.success("Good job baby. I'm so proud of you")
            st.button("Continue to Part 3", on_click=go_to_stage, args=(3,))
        else:
            st.warning("Bruh you should've gotten this one")




#part 3

elif st.session_state.stage == 3:
    st.header("Part 3:")
    st.info("So, we just got 456...")
    st.info("Your hint: BeBC") 
    period = st.number_input("Enter code:", value=0, step=1, key="input_level_3")
     
    if st.button("Unlock", key="btn_3"):
        if 30 < period < 34:
            st.success("Didn't think you'd get this one...")
            st.button("Continue to Part 4", on_click=go_to_stage, args=(4,))
        else:
            st.warning("Not Quite...")




#part 4 
elif st.session_state.stage == 4:
    st.header("Part 4:")
    st.info("So, I don't know if we have ever talked about this. But I consider this to be our first date (this one is actually a name)")
    answer = st.text_input("Enter code:", key="input_level_4")
    
    if st.button("Unlock", key="btn_4"):
        if answer.lower() == "dq":
            st.success("Good Job!")
            st.button("Continue to Part 5", on_click=go_to_stage, args=(5,))
        else:
            st.warning("C'mon bruh")




#part 5
elif st.session_state.stage == 5:
    st.header("Part 5:")
    st.info("This might be an easy one...")
    st.info("What your name is going to be one day :)")
    answer = st.text_input("Enter code:", key="input_level_5")
    
    if st.button("Unlock", key="btn_5"):
        if answer.lower() == "olivia mccormack":
            st.success("I love you so much baby. I hope you have a great birthday.")
            st.button("Continue to Final Part", on_click=go_to_stage, args=(6,))
        else:
            st.warning("Dumb Dumb")




#part 6
elif st.session_state.stage == 6:
    st.balloons()
    st.header("🎉 You Did It!")
    st.subheader("Happy Birthday!! 💖")
    
    if st.button("Play Again?"):
        go_to_stage(1)
        st.rerun()
