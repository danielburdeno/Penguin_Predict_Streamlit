import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.title('Penguin Prediction App')

@st.cache_resource
def load_model(file):
    model_file = open(file, 'rb')
    loaded_model = joblib.load(model_file)
    model_file.close()
    return loaded_model

penguin_model = load_model('penguin_dt.pkl')

st.sidebar.title('Forms')
form1 = st.sidebar.form(key='Data Inputs')
form1.subheader('Bill Length and Depth')
bill_length = form1.number_input('Enter the bill lenth (mm)', min_value=0.0)
bill_depth = form1.number_input('Enter bill depth (mm)', min_value=0.0)
form1.subheader('Flipper Length')
flipper_length = form1.number_input('Enter the flipper length (mm)', min_value=0.0)
form1.subheader('Body Mass')
body_mass = form1.number_input('Enter the body mass (g)', min_value=0.0)
form1.subheader('Sex')
sex = form1.number_input("Enter Sex", help='0 - Male, 1 - Female', min_value=0.0, max_value=1.0, step=1.0)
#sex = form1.radio(options=[0, 1], label='Sex')
form1.subheader('Island')
island = form1.selectbox('Select the island', ['Torgersen', 'Biscoe', 'Dream'])
form_button = form1.form_submit_button('Submit Features')

st.header('New Penguin Data')
new_input = np.array([island, bill_length, bill_depth, flipper_length, body_mass, sex]).reshape(1, -1)
predict_in = pd.DataFrame(new_input, columns=penguin_model.feature_names_in_)
expander_df = st.expander('View New Penguin Data')
expander_df.table(predict_in)

predict_button = st.button('Predict Penguin Species')
if predict_button:
    if float(bill_length) <= 0.0:
        st.write('These are not valid values, try again')
    else:
        prediction = penguin_model.predict(predict_in)
        st.write(f'The predicted species is {prediction[0]}')
