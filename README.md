# Feedback Analysis Application

This application is built using Streamlit and TextBlob. It allows users to add a review and performs sentiment analysis on the review text.

## Dependencies

- Streamlit
- TextBlob
- openpyxl
- datetime

## How it works

1. The application displays a title 'Feedback Analysis' and a header 'Add a review'.
2. It provides text input fields for the user's name and email, and a text area for the review.
3. When the user clicks the 'Submit' button, the application performs sentiment analysis on the review text using TextBlob.
4. The sentiment polarity score is used to determine the sentiment of the review (Very Negative, Negative, Neutral, Positive, Very Positive) and a corresponding rating (0, 1, 3, 4, 5).
5. The application also displays the polarity and subjectivity scores from TextBlob.
6. The review along with the timestamp, name, and email is then saved to an Excel file 'CustomerReview.xlsx'.

## How to run

To run this application, you need to have the above dependencies installed. You can then run the application using Streamlit:

```bash
streamlit run app.py
```
## Sample

![image](https://github.com/pragya-jain-io/Feedback-Analysis-Application/assets/101741697/dd1b3d2c-1188-4010-a078-8a821d011307)

![image](https://github.com/pragya-jain-io/Feedback-Analysis-Application/assets/101741697/1c6a3e93-94ad-42dc-a019-02b0b509c6cc)

