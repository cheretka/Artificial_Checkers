import streamlit as st




st.write("""
# Simple Stock Proce App
""")


genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

