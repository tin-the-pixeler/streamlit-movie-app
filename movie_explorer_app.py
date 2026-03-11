import streamlit as st
import pandas as pd

df = pd.read_csv("movies_cleaned.csv")
st.title("🎬 Movies Movies Movies 🎬")
all_genres = ["All"] + sorted(
    df["genres"]
    .dropna()
    .str.split("|")
    .explode()
    .str.strip()
    .unique()
    .tolist()
)

selected_genre = st.selectbox("Select a genre:", all_genres)

if selected_genre == "All":
    filtered_movies = df[["Title", "Year"]].reset_index(drop=True)
    
    filtered_movies.index += 1
else:
    filtered_movies = df[
        df["genres"].str.split("|").apply(lambda g: selected_genre in g)
    ][["Title", "Year"]].reset_index(drop=True)
    
    filtered_movies.index += 1

st.subheader(f"Movies in Genre: {selected_genre}")
st.write(f"{len(filtered_movies)} movies found.")
st.dataframe(filtered_movies, use_container_width=True)
