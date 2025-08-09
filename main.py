import streamlit as st
import langchain_helper


st.title("Restaurant Name and Menu Generator")

cuisine = st.sidebar.selectbox(
    "Choose an option",
    ("Indian", "Chinese", "Italian", "Mexican", "Japanese", "French", "Mediterranean", "Thai", "American", "Spanish")
)


if cuisine:
    response = langchain_helper.generate_restaurant_info(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].split(',')
    st.write("**Menu Items**")

    for item in menu_items:
        st.write(item)

         
  