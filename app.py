import streamlit as st
import pickle
import requests
import pandas as pd
import random
from src.remove_ import remove

st.set_page_config(page_title="Mobile Recommender System", page_icon=":📲:", layout="wide", initial_sidebar_state="expanded")

df = pickle.load(file=open(file=r'src\model\dataframe.pkl', mode='rb'))
similarity = pickle.load(file=open(file=r'src\model\similarity.pkl', mode='rb'))


remove()

def recommend_different_variety(mobile):
    mobile_index = df[df['name'] == mobile].index[0]
    similarity_array = similarity[mobile_index]
    different_variety = random.sample(list(enumerate(similarity_array)),k=10)


    recommended_mobiles_variety = []
    recommended_mobiles_IMG_variety = []
    recommended_mobiles_ratings_variety = []
    recommended_mobiles_price_variety = []
    for i in different_variety:
        recommended_mobiles_variety.append(df['name'].iloc[i[0]])
        recommended_mobiles_IMG_variety.append(fetch_IMG(i[0]))
        recommended_mobiles_ratings_variety.append(df['ratings'].iloc[i[0]])
        recommended_mobiles_price_variety.append(df['price'].iloc[i[0]])

    return recommended_mobiles_variety, recommended_mobiles_IMG_variety, recommended_mobiles_ratings_variety, recommended_mobiles_price_variety
    

def recommend(mobile):
    mobile_index = df[df['name'] == mobile].index[0]
    similarity_array = similarity[mobile_index]
    similar_10_mobiles = sorted(list(enumerate(similarity_array)), reverse=True, key=lambda x: x[1])[1:11]


    recommended_mobiles = []
    recommended_mobiles_IMG = []
    recommended_mobiles_ratings = []
    recommended_mobiles_price = []
    for i in similar_10_mobiles:
        recommended_mobiles.append(df['name'].iloc[i[0]])
        recommended_mobiles_IMG.append(fetch_IMG(i[0]))
        recommended_mobiles_ratings.append(df['ratings'].iloc[i[0]])
        recommended_mobiles_price.append(df['price'].iloc[i[0]])

    return recommended_mobiles, recommended_mobiles_IMG, recommended_mobiles_ratings, recommended_mobiles_price

def fetch_IMG(mobile_index):
    # response = requests.get(url=df['imgURL'].iloc[mobile_index])
    return df['imgURL'].iloc[mobile_index]


st.title('Mobile Recommender System')
st.markdown('> ##### ***Guide***: :choose Select a mobile phone of your choice from the available options, and upon clicking the "Recommend" button, the model will promptly showcase the most closely related mobile phones based on your selection. The recommendation system leverages similarity metrics to identify and present the mobile phones with the highest resemblance to your chosen device, enabling you to explore alternatives that align with your preferences and requirements and each time you click the recommend button the Other Variety of mobiles get updated.')

mobiles = df['name'].values
selected_mobile = st.selectbox(label='Select Mobile Name', options=mobiles)

if st.button('Recommend'):
    mobile_name, mobile_IMG, mobiles_ratings, mobiles_price = recommend(selected_mobile)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(f"<p style='text-align: center;'>{mobile_name[0]}\n"
                    f"Ratings: {mobiles_ratings[0]}  \n"
                    f"Price: {mobiles_price[0]}", unsafe_allow_html=True)
        st.image(mobile_IMG[0])

    with col2:
        st.markdown(f"<p style='text-align: center;'>{mobile_name[1]}\n"
                    f"Ratings: {mobiles_ratings[1]}  \n"
                    f"Price: {mobiles_price[1]}", unsafe_allow_html=True)
        st.image(mobile_IMG[1])

    with col3:
        st.markdown(f"<p style='text-align: center;'>{mobile_name[2]}\n"
                    f"Ratings: {mobiles_ratings[2]}  \n"
                    f"Price: {mobiles_price[2]}", unsafe_allow_html=True)
        st.image(mobile_IMG[2])

    with col4:
        st.markdown(f"<p style='text-align: center;'>{mobile_name[3]}\n"
                    f"Ratings: {mobiles_ratings[3]}  \n"
                    f"Price: {mobiles_price[3]}", unsafe_allow_html=True)
        st.image(mobile_IMG[3])

    with col5:
        st.markdown(f"<p style='text-align: center;'>{mobile_name[4]}\n"
                    f"Ratings: {mobiles_ratings[4]}  \n"
                    f"Price: {mobiles_price[4]}", unsafe_allow_html=True)
        st.image(mobile_IMG[4])

    st.markdown('---')


    col6, col7, col8, col9, col10 = st.columns(5)


    with col6:
        st.markdown(f"<p style='text-align: center;'>{mobile_name[5]}\n"
                    f"Ratings: {mobiles_ratings[5]}  \n"
                    f"Price: {mobiles_price[5]}", unsafe_allow_html=True)
        st.image(mobile_IMG[5])

    with col7:
        st.markdown(f"<p style='text-align: center;'>{mobile_name[6]}\n"
                    f"Ratings: {mobiles_ratings[6]}  \n"
                    f"Price: {mobiles_price[6]}", unsafe_allow_html=True)
        st.image(mobile_IMG[6])

    with col8:
        st.markdown(f"<p style='text-align: center;'>{mobile_name[7]}\n"
                    f"Ratings: {mobiles_ratings[7]}  \n"
                    f"Price: {mobiles_price[7]}", unsafe_allow_html=True)
        st.image(mobile_IMG[7])

    with col9:
        st.markdown(f"<p style='text-align: center;'>{mobile_name[8]}\n"
                    f"Ratings: {mobiles_ratings[8]}  \n"
                    f"Price: {mobiles_price[8]}", unsafe_allow_html=True)
        st.image(mobile_IMG[8])

    with col10:
        st.markdown(f"<p style='text-align: center;'>{mobile_name[9]}\n"
                    f"Ratings: {mobiles_ratings[9]}  \n"
                    f"Price: {mobiles_price[9]}", unsafe_allow_html=True)
        st.image(mobile_IMG[9])

    mobile_name_variety , mobile_IMG_variety , mobiles_ratings_variety , mobiles_price_variety = recommend_different_variety(selected_mobile)    

    st.markdown('---')
    st.markdown('## Other Variety of mobiles')
    st.markdown('---')

    col11, col12, col13, col14, col15 = st.columns(5)

    with col11:
        st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[0]}\n"
                    f"Ratings: {mobiles_ratings_variety[0]}  \n"
                    f"Price: {mobiles_price_variety[0]}", unsafe_allow_html=True)
        st.image(mobile_IMG_variety[0])

    with col12:
        st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[1]}\n"
                    f"Ratings: {mobiles_ratings_variety[1]}  \n"
                    f"Price: {mobiles_price_variety[1]}", unsafe_allow_html=True)
        st.image(mobile_IMG_variety[1])

    with col13:
        st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[2]}\n"
                    f"Ratings: {mobiles_ratings_variety[2]}  \n"
                    f"Price: {mobiles_price_variety[2]}", unsafe_allow_html=True)
        st.image(mobile_IMG_variety[2])

    with col14:
        st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[3]}\n"
                    f"Ratings: {mobiles_ratings_variety[3]}  \n"
                    f"Price: {mobiles_price_variety[3]}", unsafe_allow_html=True)
        st.image(mobile_IMG_variety[3])

    with col15:
        st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[4]}\n"
                    f"Ratings: {mobiles_ratings_variety[4]}  \n"
                    f"Price: {mobiles_price_variety[4]}", unsafe_allow_html=True)
        st.image(mobile_IMG_variety[4])

    col16, col17, col18, col19, col20 = st.columns(5)

    with col16:
        st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[5]}\n"
                    f"Ratings: {mobiles_ratings_variety[5]}  \n"
                    f"Price: {mobiles_price_variety[5]}", unsafe_allow_html=True)
        st.image(mobile_IMG_variety[5])

    with col17:
        st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[6]}\n"
                    f"Ratings: {mobiles_ratings_variety[6]}  \n"
                    f"Price: {mobiles_price_variety[6]}", unsafe_allow_html=True)
        st.image(mobile_IMG_variety[6])

    with col18:
        st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[7]}\n"
                    f"Ratings: {mobiles_ratings_variety[7]}  \n"
                    f"Price: {mobiles_price_variety[7]}", unsafe_allow_html=True)
        st.image(mobile_IMG_variety[7])

    with col19:
        st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[8]}\n"
                    f"Ratings: {mobiles_ratings_variety[8]}  \n"
                    f"Price: {mobiles_price_variety[8]}", unsafe_allow_html=True)
        st.image(mobile_IMG_variety[8])

    with col20:
        st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[9]}\n"
                    f"Ratings: {mobiles_ratings_variety[9]}  \n"
                    f"Price: {mobiles_price_variety[9]}", unsafe_allow_html=True)
        st.image(mobile_IMG_variety[9])

st.markdown('---')
st.markdown('> ## Made by Gyan Prakash Kushwaha')
