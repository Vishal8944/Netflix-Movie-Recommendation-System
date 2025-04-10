import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Apply custom CSS for full black background theme
st.markdown(
    """
    <style>
    html, body, [class*="st"] {
        background-color: black !important;
        color: white !important;
    }
    .stSelectbox, .stButton>button, .stTextInput>div>div>input {
        background-color: #333 !important;
        color: white !important;
        border-radius: 5px;
    }
    .stMarkdown, .stTitle, .stHeader, .stText, .stButton, .stSelectbox, .stTextInput {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load dataset
def load_data():
    df = pd.read_csv("net.csv")  # Update with correct file path if needed
    df.dropna(subset=['title', 'genres'], inplace=True)
    return df

# Compute similarity matrix
def compute_similarity(df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['genres'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

# Recommend movies
def recommend_movie(title, df, cosine_sim):
    if title not in df['title'].values:
        return ["Movie not found!"]
    
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    
    recommended_titles = df['title'].iloc[movie_indices].tolist()
    return recommended_titles

# Streamlit UI
st.sidebar.write("About the Recommendation System")
st.sidebar.write("This movie recommendation system suggests similar movies based on genres. It uses a Content-Based Filtering approach, computing cosine similarity between movie genres to recommend the most relevant films.")

st.title("Movie Recommendation System")
df = load_data()
cosine_sim = compute_similarity(df)

movie_name = st.selectbox("Select a movie:", df['title'].unique())
if st.button("Recommend"):
    recommendations = recommend_movie(movie_name, df, cosine_sim)
    st.write("Recommended Movies:")
    
    for movie in recommendations:
        st.write(movie)
