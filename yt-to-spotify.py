import os
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def format_filename(filename):
    # Remove file extension
    name = os.path.splitext(filename)[0]

    # Try to split artist and song name
    parts = re.split(r'\s*-\s*', name, 1)

    if len(parts) == 2:
        artist, song = parts
    else:
        # If can't split, assume the whole name is the song title
        artist = "Unknown Artist"
        song = name

    # Remove any extra spaces and non-alphanumeric characters
    artist = re.sub(r'[^\w\s]', '', artist).strip()
    song = re.sub(r'[^\w\s]', '', song).strip()

    return f"{artist} - {song}"

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(('.m4a', '.mkv', '.mpg', '.mp4', '.avi', '.webm')):
            new_name = format_filename(filename)
            extension = os.path.splitext(filename)[1]
            new_filename = f"{new_name}{extension}"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed: {filename} -> {new_filename}")

def create_spotify_playlist(directory):
    # Set up Spotify API credentials
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
        scope="playlist-modify-private"
    ))

    # Create a new private playlist
    user_id = sp.me()['id']
    playlist = sp.user_playlist_create(user_id, "My YouTube Favorites", public=False)

    # Search for and add tracks to the playlist
    tracks_to_add = []
    for filename in os.listdir(directory):
        if filename.endswith(('.m4a', '.mkv', '.mpg', '.mp4', '.avi', '.webm')):
            name = os.path.splitext(filename)[0]
            results = sp.search(q=name, type='track', limit=1)

            if results['tracks']['items']:
                track_uri = results['tracks']['items'][0]['uri']
                tracks_to_add.append(track_uri)
                print(f"Found on Spotify: {name}")
            else:
                print(f"Could not find on Spotify: {name}")

            # Add tracks in batches of 100
            if len(tracks_to_add) == 100:
                sp.user_playlist_add_tracks(user_id, playlist['id'], tracks_to_add)
                print(f"Added 100 tracks to playlist")
                tracks_to_add = []
                time.sleep(1)  # Add a small delay to avoid rate limiting

    # Add any remaining tracks
    if tracks_to_add:
        sp.user_playlist_add_tracks(user_id, playlist['id'], tracks_to_add)
        print(f"Added {len(tracks_to_add)} tracks to playlist")

def main():
    directory = input("Enter the directory path of your video files: ")
    rename_files(directory)
    create_spotify_playlist(directory)

if __name__ == "__main__":
    main()
