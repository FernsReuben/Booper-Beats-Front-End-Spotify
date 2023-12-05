"""
Written By: Reuben Fernandes
Date: 11/11/2023
Description: A music player using the Spotify API. 
⠀⠀⠀⠀⢀⣤⡀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠉⢻⠟⢹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣿⡄⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⣠⣤⣄⠀⠀⠀⠀
⠀⠀⣰⡿⠋⠀⣀⣀⠈⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠘⠋⠀⣿⠇⠀⠀⠀
⠀⣠⡟⠀⢀⣾⠟⠻⠿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⣾⠋⢀⣀⠈⠻⢶⣄⠀⠀
⢠⣿⠁⣰⡿⠁⠀⣀⣤⣶⣶⡶⢶⣤⣄⡀⢀⣠⠴⠚⠉⠉⠉⠉⠉⠙⢶⡄⠛⠒⠛⠙⢳⣦⡀⠹⣆⠀
⢸⡇⢠⣿⣠⣴⣿⡟⢉⣠⠤⠶⠶⠾⠯⣿⣿⣧⣀⣤⣶⣾⣿⡿⠿⠛⠋⢙⣛⡛⠳⣄⡀⠙⣷⡀⢹⡆
⢸⠀⢸⣿⣿⣿⣿⠞⠉⠀⠀⠀⠀⣀⣤⣤⠬⠉⠛⠻⠿⠟⠉⢀⣠⢞⣭⣤⣤⣍⠙⠺⢷⡀⢸⡇⠀⣿
⢸⠀⢸⣿⣿⡟⠀⠀⠀⢀⣠⠞⣫⢗⣫⢽⣶⣤⣀⠉⠛⣶⠖⠛⠀⣾⡷⣾⠋⣻⡆⠀⠀⡇⣼⠇⠀⣿
⢸⠀⠀⣿⣿⡇⢠⡤⠔⣋⡤⠞⠁⢸⣷⣾⣯⣹⣿⡆⢀⣏⠀⠈⠈⣿⣷⣼⣿⠿⠷⣴⡞⠀⣿⠀⠀⣿
⢸⠀⠀⢿⣿⡇⠀⠀⠘⠻⠤⣀⡀⠸⣿⣯⣿⣿⡿⠷⠚⠉⠛⠛⠛⠛⠉⠉⠀⣠⡾⠛⣦⢸⡏⠀⠀⣿
⢸⠀⠀⢸⣿⡇⠀⣠⠶⠶⠶⠶⠿⣿⣭⣭⣁⣀⣠⣤⣤⣤⣤⣤⣤⡶⠶⠛⠋⢁⣀⣴⠟⣽⠇⠀⠀⣿
⢸⠀⠀⢸⣿⡇⢾⣅⠀⠀⠶⠶⢦⣤⣤⣀⣉⣉⣉⣉⣁⣡⣤⣤⣴⡶⠶⠶⠚⠉⢉⡿⣠⠟⠀⠀⣰⡟
⢸⡀⠀⠀⢿⣇⠀⠈⠛⠳⠶⠤⠤⢤⣀⣉⣉⣉⣉⣉⣉⣁⣀⣠⣤⡤⠤⠤⠶⠞⢻⡟⠃⠀⠀⣰⠟⠀
⢸⣧⠀⠀⠘⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⣠⣤⣶⣿⣧⣀⣴⠟⠃⠀⠀
⠀⢻⣆⠀⠀⠈⢻⣿⣿⣷⣶⣤⣄⣀⣀⣀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣟⡉⠀⠀⠀⠀⠀
⠀⠀⢻⣦⡄⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀
⠀⢀⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀

11.11.2023.0145-- Only implemented Playlists so far. Menu works, music player isn't tested yet. Need to find a way to bypass the authentication process for premium access. Will look into it later. Committing for now to save progress and to get repo started. - RF

11.11.2023.1813-- Added the ability to search for playlists and play them. Also added the ability to search for tracks and add them to a playlist. - RF

11.19.2023.2130-- hit a roadblock. went back and reimplemented from scratch. playlists work. will work on searching and adding tracks to playlists next. - RF
"""

import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from pyfiglet import figlet_format  # pip install pyfiglet


# Assuming you are using the default cache path
cache_path = ".cache"
if os.path.exists(cache_path):
    os.remove(cache_path)

# Spotify API credentials
CLIENT_ID = "0d0fa1cb002742e2af55ffc57265278f"
CLIENT_SECRET = "86588df1a2924918b37a6ab61dd72002"
REDIRECT_URI = "http://localhost:8888/callback"

# Spotify API scope
SCOPE = "user-library-read user-read-playback-state user-modify-playback-state playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public"

# Initialize Spotipy with authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI, scope=SCOPE))

def play_preselected_playlist(playlist_uri, shuffle=False):
    try:
        sp.start_playback(context_uri=playlist_uri)
        print(f"Playback started for playlist: {playlist_uri}")

        if shuffle:
            sp.shuffle(state=True)
            print("Shuffle play enabled.")
    except spotipy.SpotifyException as e:
        print(f"Error starting playback: {e}")

def play_preselected_playlist(playlist_uri, shuffle=False):
    try:
        sp.start_playback(context_uri=playlist_uri)
        print(f"Playback started for playlist: {playlist_uri}")

        if shuffle:
            sp.shuffle(state=True)
            print("Shuffle play enabled.")
    except spotipy.SpotifyException as e:
        print(f"Error starting playback: {e}")

def search_for_track(query):
    results = sp.search(q=query, type='track', limit=10)
    tracks = results['tracks']['items']
    return tracks

def select_track_from_results(tracks):
    print("Search Results:")
    for i, track in enumerate(tracks):
        print(f"{i + 1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")

    index = int(input("Enter the track index to select: ")) - 1

    if 0 <= index < len(tracks):
        selected_track = tracks[index]
        track_uri = selected_track['uri']
        return track_uri
    else:
        print("Invalid track index.")
        return None

def search_for_track_and_select():
    query = input("Enter the track name: ")
    tracks = search_for_track(query)

    if not tracks:
        print("No tracks found.")
        return None

    selected_track_uri = select_track_from_results(tracks)

    return selected_track_uri

def search_and_add_to_playlist(playlist_uri):
    track_uri = search_for_track_and_select()

    if track_uri:
        try:
            sp.playlist_add_items(playlist_uri, items=[track_uri])
            print(f"Track added to playlist: {playlist_uri}")
        except spotipy.SpotifyException as e:
            print(f"Error adding track to playlist: {e}")

def get_album_artwork(track_uri):
    track_info = sp.track(track_uri)
    return track_info['album']['images'][0]['url']

# Pre-selected playlist URIs
preselected_playlists = [
    "spotify:playlist:7Gk8MHzbGL1dyrEpCM6jgB",
    "spotify:playlist:3P2XUd8YlIQYCA6rECPGeN",
    "spotify:playlist:2mQ7IDZLJWImfQ9uFLAdDF",
    # Add more pre-selected playlist URIs as needed
]

def control_playback(action):
    if action == 'play':
        sp.start_playback()
    elif action == 'pause':
        sp.pause_playback()
    elif action == 'next':
        sp.next_track()
    elif action == 'previous':
        sp.previous_track()
    else:
        print("Invalid action. Please enter play/pause/next/previous.")

# Main loop for the music player
while True:
    print(figlet_format("Booper Beats", font="poison"))
    print("Music Player Menu:")
    print("1. Play Pre-selected Playlist 1")
    print("2. Play Pre-selected Playlist 2")
    print("3. Play Pre-selected Playlist 3")
    print("4. Control playback (play/pause/next/previous)")
    print("5. Search for track by URI and add to Playlist 3")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        playlist_uri = preselected_playlists[0]
        play_preselected_playlist(playlist_uri, shuffle=True)
    elif choice == "2":
        playlist_uri = preselected_playlists[1]
        play_preselected_playlist(playlist_uri, shuffle=True)
    elif choice == "3":
        playlist_uri = preselected_playlists[2]
        play_preselected_playlist(playlist_uri, shuffle=True)
    elif choice == "4":
        action = input("Enter the action (play/pause/next/previous): ")
        control_playback(action)
    elif choice == "5":
        track_uri = search_and_add_to_playlist(preselected_playlists[2])
        if track_uri:
            artwork_url = get_album_artwork(track_uri)
            print(f"Album Artwork URL: {artwork_url}")
            # Now, you can use the 'artwork_url' to display the album artwork in Anvil
    elif choice == "6":
        print("Exiting the Music Player.")
        break
    else:
        print("Invalid choice. Please try again.")