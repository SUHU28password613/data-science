import streamlit as st


st.title("Simple Calculator")
#st.subheader("Using Streamlit")
st.markdown("This is a simple calculator app  using Streamlit.")
#st.render("This is a simple calculator app using Streamlit.")


c1,c2 = st.columns(2)
fnum = c1.number_input("First Number", value=0)
snum = c2.number_input("Second Number", value=0)

options = ["Add", "Subtract", "Multiply", "Divide"]
choice = st.radio("Select Operation", options)

button = st.button("Calculate")

result = 0
if button:
    if choice == "Add":
        result = fnum + snum
    elif choice == "Subtract":
        result = fnum - snum
    elif choice == "Multiply":
        result = fnum * snum
    elif choice == "Divide":
        result = fnum / snum
   
st.warning(f'Result:{result}')

st.snow()