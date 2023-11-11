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
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pyfiglet import figlet_format  # pip install pyfiglet
     


# Spotify API credentials
CLIENT_ID = "CLIENT ID HERE"
CLIENT_SECRET = "SECRET ID HERE"
REDIRECT_URI = "WEB APP URI HERE"

# Spotify API scope
SCOPE = "user-library-read user-read-playback-state user-modify-playback-state"

# Initialize Spotipy with authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI, scope=SCOPE))

def search_for_playlist(query):
    results = sp.search(q=query, type='playlist')
    playlists = results['playlists']['items']
    return playlists

def search_for_track(query):
    results = sp.search(q=query, type='track')
    tracks = results['tracks']['items']
    return tracks

def add_track_to_playlist(track_uri, playlist_id):
    sp.playlist_add_items(playlist_id, items=[track_uri])
    print(f"Track added to playlist.")

def play_playlist(playlist_uri, shuffle=False):
    try:
        sp.start_playback(context_uri=playlist_uri)
        print(f"Playback started for playlist: {playlist_uri}")

        if shuffle:
            sp.shuffle(state=True)
            print("Shuffle play enabled.")
    except spotipy.SpotifyException as e:
        print(f"Error starting playback: {e}")

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

# Initialize an array to store playlist URIs
playlist_uris = ["YOUR PLAYLIST URIS HERE"]

# Main loop for the music player
while True:
    print( figlet_format("Booper Beats", font = "poison" ) )
    print("Music Player Menu:")
    print("1. Search for a playlist")
    print("2. Play a playlist by index")
    print("3. Play a custom playlist by index")
    print("4. Shuffle play a custom playlist by index")
    print("5. Search for a track and add to playlist")
    print("6. Control playback (play/pause/next/previous)")
    print("7. Exit")
     


    choice = input("Enter your choice: ")

    if choice == "1":
        query = input("Enter the playlist name: ")
        playlists = search_for_playlist(query)
        for i, playlist in enumerate(playlists):
            print(f"{i+1}. {playlist['name']} by {playlist['owner']['display_name']}")
    elif choice == "2":
        index = int(input("Enter the playlist index: ")) - 1
        if 0 <= index < len(playlists):
            playlist_uri = playlists[index]['uri']
            play_playlist(playlist_uri)
    elif choice == "3":
        if playlist_uris:
            for i, uri in enumerate(playlist_uris):
                print(f"{i+1}. Custom Playlist {i+1}")
            index = int(input("Enter the custom playlist index: ")) - 1
            if 0 <= index < len(playlist_uris):
                play_playlist(playlist_uris[index], shuffle=True)
            else:
                print("Invalid custom playlist index.")
        else:
            print("No custom playlists available. Please add some first.")
    elif choice == "4":
        if playlist_uris:
            for i, uri in enumerate(playlist_uris):
                print(f"{i+1}. Custom Playlist {i+1}")
            index = int(input("Enter the custom playlist index: ")) - 1
            if 0 <= index < len(playlist_uris):
                play_playlist(playlist_uris[index], shuffle=True)
            else:
                print("Invalid custom playlist index.")
        else:
            print("No custom playlists available. Please add some first.")
    elif choice == "5":
        query = input("Enter the track name: ")
        tracks = search_for_track(query)
        for i, track in enumerate(tracks):
            print(f"{i+1}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")

        index = int(input("Enter the track index to add to playlist: ")) - 1
        if 0 <= index < len(tracks):
            track_uri = tracks[index]['uri']

            # Replace 'your_playlist_id' with the actual ID of the playlist where you want to add the track
            add_track_to_playlist(track_uri, 'your_playlist_id')
    elif choice == "6":
        action = input("Enter the action (play/pause/next/previous): ")
        control_playback(action)
    elif choice == "7":
        print("Exiting the Music Player.")
        break
    else:
        print("Invalid choice. Please try again.")
