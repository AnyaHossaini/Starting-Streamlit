import streamlit as st

st.header('Press the buton')

if st.button('Happy Halloween'):
    st.write('BOO')

else:
    st.write('Trick or treat')
