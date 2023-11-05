import streamlit as st

st.write("""
         # Getting to know you
         """)

st.header('Feelings: ')

st.write('How do you feel today ?')

if st.button('😄'):
    st.write("You must feel happy today")
     
if st.button('😍'):
    st.write("You must feel loved today")
    
if st.button('😎'):
    st.write("You must feel cool today")
    
if st.button('😔'):
    st.write("You must feel sad today")
    
if st.button('😣'):
    st.write("You must feel anxious today")
    
st.header('Colors: ')

st.write('Which is your faovirte color')

if st.button(":blue[blue]"):
    st.write("Your sensitive and reliable side, with a consistent effort to think of others")

if st.button(":green[green]"):
    st.write("You are typically down to earth and aware of what other people think of you, seeking acknowledgement and acceptance for the everyday things you do")

if st.button(":orange[orage]"):
    st.write("You have a great need for socialization and a desire for human companionship")
    
if st.button(":red[red]"):
    st.write("you are bold, boisterous, and full of energy")

if st.button(":violet[violet]"):
    st.write("you are sensitive and compassionate, understanding and supportive, thinking of others before yourself")
    
if st.button(":grey[grey]"):
    st.write("you are neutral about life, often to the point of being indifferent")
    
if st.button(":rainbow[rainbow]"):
    st.write("All the above from the other colors")