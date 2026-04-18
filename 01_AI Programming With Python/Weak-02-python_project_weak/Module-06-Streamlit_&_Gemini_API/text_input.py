import streamlit as st

st.write("Hello, Streamlit!")

st.title("Streamlit Text Input Example")
st.header("Content 1",divider=True) 
st.subheader("Content 3",divider=True)
st.text("Content 2")
st.markdown("**Content 4**")
st.markdown("**:red[Content 4]**")
st.markdown(":orange-background[**:red[Content 4]**] :smiling_face_with_three_hearts:")

a=10 
b=20
st.write("The value of a is",a)
st.write("The value of b is",b)