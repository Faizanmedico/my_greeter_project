# app.py

import streamlit as st

def main():
    st.title("👋 My Greeter Project")
    st.write("Welcome to the Greeter App!")

    # Input field for name
    name = st.text_input("Enter your name:")

    # Button to trigger greeting
    if st.button("Greet Me"):
        if name:
            st.success(f"Hello, {name}! 👋 Hope you're having a great day!")
        else:
            st.warning("Please enter your name first.")

if __name__ == "__main__":
    main()
