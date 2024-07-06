import streamlit as st
import pickle
import pandas as pd

# Streamlit run test_app.py
def recommend(movie):
    # Get the movie index
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    # Get the list of movies with distances and sort them
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies

# Load the movie list and similarity matrix
movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Define the CSS for the background image or color
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://static.vecteezy.com/system/resources/thumbnails/001/227/430/small/empty-theater-or-cinema-stage.jpg"); /* Change this URL to your image */
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    height: 100%;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write('Recommended Movies:')
    for movie in recommendations:
        st.write(movie)

# Informing users about the unavailability of movie posters
st.markdown('<p style="color:red;">Note: Due to a government ban on the TMDB API, movie posters cannot be fetched and displayed.</p>', unsafe_allow_html=True)

# Display "Made by Amit"
st.markdown('<p style="text-align: center;">Made by Amit ✌️</p>', unsafe_allow_html=True)
