import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #ffffff;
        font-size: 20px;
        font-family: 'Arial', sans-serif;
    }
    .stTitle {
        font-size: 50px;
        color: #ff6347; /* Red color for title */
        text-align: center;
        margin-bottom: 30px;
    }
    .stSelectbox label {
        font-size: 25px;
        color: #ffffff;
    }
    .stButton button {
        font-size: 25px;
        background-color: #ff6347;
        color: #ffffff; /* White color for button text */
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: #ff6347; /* Hover color */
        color: #000000; /* Text color on hover */
    }
    .stButton button:active {
        background-color: #ff6347 !important;
        color: #ffffff !important;
    }
    .stText {
        font-size: 20px;
        text-align: center;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
    }
    .stImage {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="stTitle">Movie Recommender System</h1>', unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    "Could you recommend a good movie to watch?",
    movies['title'].values,
    format_func=lambda x: x[:50] + '...' if len(x) > 50 else x  # Truncate long names
)

if st.button('Recommend', key='recommend_button'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
