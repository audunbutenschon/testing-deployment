import streamlit as st

def main():
    st.title('My Streamlit App')

    # Text Input
    user_input = st.text_input("Enter some text")

    # Slider
    slider_val = st.slider('Select a range', 0.0, 100.0, (25.0, 75.0))

    # Checkbox
    checkbox_val = st.checkbox('Check me out')

    # Button
    if st.button('Press Me'):
        st.write('You pressed the button!')

    # Display user selections
    st.write(f'You entered: {user_input}')
    st.write(f'You selected a range from {slider_val[0]} to {slider_val[1]}')
    st.write(f'Checkbox is {"checked" if checkbox_val else "not checked"}')

if __name__ == "__main__":
    main()
