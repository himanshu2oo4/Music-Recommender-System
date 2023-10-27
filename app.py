import pickle 
import streamlit as st 
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials

st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

# initialize the spotify client

client_credentials_manager = SpotifyClientCredentials(client_id= CLIENT_ID , client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager= client_credentials_manager)


def song_album_cover(song_name, artist_name):
    search_query = f'track:{song_name}, artist:{artist_name}'
    result = sp.search(q=search_query, type='track')

    if result and result['tracks']['items']:
        track = result['tracks']['items'][0]
        album_cover_url = track['album']['images'][0]['url']
        print(f"Album Cover URL for {song_name} by {artist_name}: {album_cover_url}")
        return album_cover_url
    else:
        print(f"No result found for {song_name} by {artist_name}")
        return 'https://i.postimg.cc/0QNxYz4V/social.png'
  



def recommend(song ):
  index = music[music['song'] == song].index[0]
  distances= sorted(list(enumerate(similarity[index])), reverse = True , key = lambda x : x[1])
  recommended_music_names = []
  recommended_music_posters = []
  for i in distances[1:11]:
    # fetching the movie posters 

    artist  = music.iloc[i[0]].artist 
    print(artist)
    print(music.iloc[i[0]].song)
    recommended_music_posters.append(song_album_cover(music.iloc[i[0]].song , artist))
    recommended_music_names.append(music.iloc[i[0]].song) 

  return recommended_music_names , recommended_music_posters 

st.header("Music Recommendation system")
music = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
music_list = music['song'].values

selected_music= st.selectbox('Type or Select a song ', music_list)
if st.button('show Recommendations '):
  names , posters = recommend(selected_music)
  # col1 , col2 , col3 , col4 , col5 = st.columns(5)
     
  # with col1 : 
  #   st.text(names[0])
  #   st.image(posters[0])
  # with col2 : 
  #   st.text(names[1])
  #   st.image(posters[1])
  # with col3  :
  #   st.text(names[2])
  #   st.image(posters[2])
  # with col4 : 
  #   st.text(names[3])
  #   st.image(posters[3])
  # with col5 : 
  #   st.text(names[4])
  #   st.image(posters[4])
    

  num_recommendations = len(names)
  num_cols = 5
  num_rows = 2 

  for i in range(2):
     cols = st.columns(num_cols)
     for j in range(num_cols):
        idx = i*num_cols + j 
        with cols[j] :
           st.text(names[idx])
           st.image(posters[idx])
           



