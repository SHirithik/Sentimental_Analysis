import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from streamlit_extras.let_it_rain import rain

analyzer = SentimentIntensityAnalyzer()

st.title("Sentiment Analysis")

message = st.text_area("Enter Your Text")

if st.button("Analyse the Sentiment"):
    scores = analyzer.polarity_scores(message)
    polarity = scores['compound']

    if polarity < 0:
        st.warning("Ouch! Your text contains negative sentiment.")
        rain(
            emoji="💔",
            font_size=30,
            falling_speed=3,
            animation_length="infinite"
        )
        st.image("sad_images.jpg", caption="Negative Statement")
    elif polarity >= 0:
        st.success("Wonderful! Your text contains positive sentiment.")
        rain(
            emoji="😍",
            font_size=30,
            falling_speed=3,
            animation_length="infinite"
        )
        st.image("happy_image.jpg", caption="Positive Sentiment")

    st.write(scores)
