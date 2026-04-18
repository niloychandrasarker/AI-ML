import streamlit as st


st.title("Streamlit Input Element Example")
st.divider()
name = st.text_input("Enter your name", placeholder="Type your name here")
email = st.text_input("Enter your email", placeholder="Type your email here")

selected_option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"],index=0,accept_new_options=True)

pressed = st.button("Submit")

if pressed:
    st.write("Your name is:", name)
    st.write("Your email is:", email)
    st.write("You selected:", selected_option)
# age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
# print(type(age))
# st.write("Your age is:", age)

# password = st.text_input("Enter your password", type="password", placeholder="Type your password here")
# st.write("Your password is:", password)