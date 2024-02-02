import streamlit as st

st.title('Streamlit: Penguins Dataset')
st.header('This is a header')
st.subheader('This is a subheader')

st.sidebar.title('Sidebar Title')
sidebar = st.sidebar
sidebar.subheader('Test')

side_button = st.sidebar.button('Press me!')
if side_button:
    sidebar.write('You pressed me!')
else:
    sidebar.write('Not pressed')

col1, col2 = st.columns(2)
col1.subheader('Col1')
col2.subheader('Col2')

col21, col22, col23 = st.columns([3, 2, 1])
col21.write('Widest Column, testing 123, text should wrap, some more text')
col22.write('Medium column width, mic check, please wrap')
col23.write('Smallest column, success')

col2.write('Back to 2 columns')

st.markdown('Markdown *syntax* works')

'## Just markdown text'

st.write('<h2 style="text-align:center"> Text aligned with HTML </h2>', unsafe_allow_html=True)

check = st.checkbox('Check me out')
button_check = st.button('Is box checked?')
if button_check:
    if check:    
        st.write('Box is checked')
    else:
        st.write('Box is not checked')

animal_options = ['Penguin', 'Dog', 'Cat', 'Horse']
fav_animal = st.radio('What is your favorite animal?', animal_options)
fav_button = st.button('Submit')
if fav_button:
    st.write(f'Your favorite animal is a {fav_animal}')

fav_animal2 = st.selectbox('What is your favorite animal?', animal_options)
fav_button2 = st.button('Submit2')
if fav_button2:
    st.write(f'Your favorite animal is a {fav_animal2}')

multi_animal = st.multiselect('What are your favorite animals?', animal_options)
multi_button = st.button('Submit3')
if multi_button:
    st.write(multi_animal)

num_pets = st.number_input('How many pets do you have?', min_value=0, max_value=10, value=0)
st.write(f'You have {num_pets} pets')

st.write('You can also use a slider')
num_pets_slider = st.slider('How many pets do you have?', 0, 10, step=1)
st.write(f'You have {num_pets_slider} pets')

in_text = st.text_input("What is your pet's name?", value="I don't have a pet")
st.write("Pet's name is:", in_text)





