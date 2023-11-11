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
    print("5. Control playback (play/pause/next/previous)")
    print("6. Exit")
     


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
        action = input("Enter the action (play/pause/next/previous): ")
        control_playback(action)
    elif choice == "6":
        print("Exiting the Music Player.")
        break
    else:
        print("Invalid choice. Please try again.")

"""
MM.DD.YYYY.TTTT - Description of changes made.
11.11.2023.0145-- Only implemented Playlists so far. Menu works, music player isn't tested yet. Need to find a way to bypass the authentication process for premium access. Will look into it later. Committing for now to save progress and to get repo started. - RF
"""