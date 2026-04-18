# Problem 1
# Create a calculator using Streamlit:
# Two number inputs
# A selectbox for operations (+, -, *, /)
# Display the result when a button is clicked
import streamlit as st
st.title("Simple Calculator")
number1 = st.number_input("Enter the first number")
number2 = st.number_input("Enter the second number")
operation = st.selectbox("Select an operation", ["+", "-", "*", "/"])

calculate = st.button("Calculate")
if calculate:
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            st.error("Cannot divide by zero")
            result = None

    if result:
        st.write(f"The result of {number1} {operation} {number2} is: {result}")



