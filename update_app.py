import streamlit as st
import pickle

model = pickle.load(open('model_DT.pkl', 'rb'))


st.title('Fake News AI')
input_news = st.text_area('Enter the News')

if st.button('Predict'):
    # 2. predict
    result = model.predict([input_news])[0]
    
    # 3. Display
    if result == 1:
        st.header("True")
    else:
        st.header("Fake")