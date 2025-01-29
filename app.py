from ytmusicapi import YTMusic
from ytmusicapi.setup import OAuthCredentials
from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

def get_spotify_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET,
    }
    response = requests.post(url, headers=headers, data=data)
    spotify_access_token = response.json().get("access_token")
    return spotify_access_token


def get_spotify_playlist(playlist_id, access_token, offset, limit):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    print(f"Offset: {offset}, Limit: {limit}")
    headers = { "Authorization": f"Bearer {access_token}" }
    params = { 
        "fields": "items.track.name,items.track.artists.name", 
        "offset": offset,
        "limit": limit
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

tracks = []
spotify_access_token = get_spotify_access_token()
for i in range(0, 501, 100):
    playlist = get_spotify_playlist("0jBqCZK8w6HXvnXRbIexem", spotify_access_token, i, 100)
    page_tracks = playlist.get("items")
    tracks.extend(page_tracks)

ytmusic = YTMusic()
video_ids = []

total_tracks = len(tracks)
print(f"Total Spotify tracks: {total_tracks}")
current_track = 0
for track in tracks:
    current_track += 1
    if current_track % 10 == 0:
        print(f"Processed {current_track} of {total_tracks} tracks")
    track_name = track.get("track").get("name")
    artist_name = track.get("track").get("artists")[0].get("name")
    search_results = ytmusic.search(f"{track_name} {artist_name}")
    if search_results:
        video_ids.append(search_results[0].get("videoId"))
    else:
        print(f"Could not find {track_name} {artist_name}")

total_yt_video_ids = [video_id for video_id in video_ids if video_id is not None]

yt_video_ids = list(dict.fromkeys(total_yt_video_ids))
print(f"Total yt_video_ids: {len(total_yt_video_ids)}")
print(f"Total unique_yt_video_ids: {len(yt_video_ids)}")
yt_video_ids_chunks = [yt_video_ids[i:i+400] for i in range(0, len(yt_video_ids), 400)]

ytmusic = YTMusic("oauth.json", oauth_credentials=OAuthCredentials(client_id=GOOGLE_CLIENT_ID, client_secret=GOOGLE_CLIENT_SECRET))
playlist_id = ytmusic.create_playlist("Bollywood Replica", "Copied from Spotify")
for yt_video_ids_chunk in yt_video_ids_chunks:
    response = ytmusic.add_playlist_items(playlist_id, yt_video_ids_chunk)
    status = response.get('status')
    if(status != 'STATUS_SUCCEEDED'):
        dialog = response.get('actions').get("confirmDialogEndpoint").get("content").get("confirmDialogRenderer").get("dialogMessages")[0].get("runs")[0].get("text")
        print(f"Failed to add songs to playlist with dialog: {dialog}")
        break

    print(f"Status: {status}")
    print(f"Added {len(yt_video_ids_chunk)} songs to playlist")
    time.sleep(5)

print(f"Playlist created and songs added to playlist_id: {playlist_id} with {len(yt_video_ids)} songs")