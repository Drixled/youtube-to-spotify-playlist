# YouTube to Spotify Playlist

This Python script automates the process of creating a Spotify playlist from a collection of locally stored music videos. It's perfect for music enthusiasts who want to easily transfer their favorite songs from downloaded YouTube videos to a Spotify playlist.

## Features

- Renames local video files to a consistent format (Artist - Song Title)
- Creates a private Spotify playlist named "My YouTube Favorites"
- Searches Spotify for each song and adds matches to the playlist
- Handles large collections by adding songs in batches (to respect API limits)
- Provides progress feedback during the process
- Uses environment variables for secure credential management

## Requirements

- Python 3.6+
- Spotify account
- Spotify Developer application credentials

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/youtube-to-spotify-playlist.git
   cd youtube-to-spotify-playlist
   ```

2. Install the required Python packages:
   ```
   pip install spotipy python-dotenv
   ```

3. Set up your Spotify Developer application:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Create a new application
   - Set the redirect URI to `http://localhost:8888/callback`
   - Note your Client ID and Client Secret

4. Create a `.env` file in the project root directory with your Spotify credentials:
   ```
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here
   SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
   ```
   Replace `your_client_id_here` and `your_client_secret_here` with your actual Spotify application credentials.

## Usage

Run the script:
```
python youtube_to_spotify.py
```

When prompted, enter the full path to the directory containing your video files.

The script will rename your files, create a new Spotify playlist, and add the songs it finds to this playlist.

## Limitations

- The script relies on filenames to search for songs on Spotify. If filenames are not accurate or songs are not available on Spotify, they won't be added to the playlist.
- Due to API rate limits, processing a large number of files may take some time.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/youtube-to-spotify-playlist/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Disclaimer

This tool is for personal use only. Ensure you have the right to use any copyrighted material. The developers are not responsible for any misuse of this script.
