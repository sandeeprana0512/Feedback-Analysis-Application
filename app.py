import streamlit as st
from textblob import TextBlob

st.title('Feedback Analysis')
st.header('Add a review')
#rating = st.select_slider('Enter rating:',options=[0,1,2,3,4,5])
name = st.text_input('Name:')
email = st.text_input('Email')
text = st.text_area('Your review:')

from openpyxl import Workbook, load_workbook
from datetime import datetime

Subjectivity =  TextBlob(text).sentiment.subjectivity
score = TextBlob(text).sentiment.polarity


if st.button('Submit'):
    if score <= -0.5:
        st.header('Very Negative')
        st.header('Rating: 0')
    elif score > -0.5 and score < 0:
        st.header('Negative') 
        st.header('Rating: 1')
    elif score > 0 and score < 0.5:
        st.header('Positive')
        st.header('Rating: 4')
    elif score >= 0.5:
        st.header('Very Positive')
        st.header('Rating: 5')
    else:
        st.header('Neutral')
        st.header('Rating: 3')
    
    st.write('TextBlob Results:')
    st.write('Polarity score:',score)
    st.write('Subjectivity score:',Subjectivity)
    
    
    wb= load_workbook('CustomerReview.xlsx')
    ws = wb.active
    review= text
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ws.append([timestamp,name,email,review])
    wb.save("CustomerReview.xlsx")

    
