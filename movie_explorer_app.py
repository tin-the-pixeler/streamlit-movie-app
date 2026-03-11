import streamlit as st
import pandas as pd

df = pd.read_csv("movies_cleaned.csv")

st.title("🎬 Movie Explorer App")

all_genres = sorted(
    df["genres"]
    .dropna()
    .str.split("|")
    .explode()
    .str.strip()
    .unique()
    .tolist()
)

selected_genre = st.selectbox("Select a genre:", all_genres)

filtered_movies = df[
    df["genres"].str.split("|").apply(lambda g: selected_genre in g)
][["Title", "Year", "genres"]].reset_index(drop=True)

st.subheader(f"Movies in Genre: {selected_genre}")
st.write(f"{len(filtered_movies)} movies found.")
st.dataframe(filtered_movies, use_container_width=True)
