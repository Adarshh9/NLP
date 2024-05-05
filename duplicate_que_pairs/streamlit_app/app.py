import streamlit as st
import helper
import pickle

with open('models/cv.pkl','rb') as file:
    cv = pickle.load(file)
with open('models/rf_model.pkl','rb') as file:
    model = pickle.load(file)

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2,cv)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')