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

# total_yt_video_ids = ['BmUe3-sfr7E', 'kPufn1grFCQ', 'PimKrn3XkuU', 'eSxo4l-epv8', '6BYIKEH0RCQ', '9-LH8ABADdo', 'PFVwNbhVqkw', 'r9eGi0rVxBw', '97NWNz9kgxU', 'ehqN6oTpmb8', 'IIg8H60bRJo', 'ru_5PA8cwkE', 'UcqI3uBKgTg', 'gmXlGQAg400', 'qTsAdjULqwg', 'xKK_5DT2pLU', 'BWDiVU38lKg', 'n0PoVxBMUyE', '_-t-FcK_9mo', 'G-pRQFsHUo0', 'vEi8i-LATnc', 'maKDIvUVkQo', '5PbWtDGOL8A', 'R0XjwtP_iTY', 'WuMWwPHTSoY', 'gnrSX7TQJqU', '3lStGpkFD10', 'DmsOinqrPvQ', 'DwUgoUhgzLo', 'Mo5tQDcs__g', 'HoDgYV1NzAI', 'ztPa6vkM-yY', 'avuWWztS-6k', 'BE8_rNJOQ-0', 'ctJI7pCbxAo', 'qe_klgHMoDY', 'smn3mDBOUy4', 'SS3lIQdKP-A', 'asw-wTDzGUQ', 'xHLnZMjJ8bY', '_ybTzGoNRjw', 'acdKE2hja7w', '3kKCLE3CPL0', 'YhUAM0oNWB0', '0zF-yRUdEA0', 'rR1Gs1ckl_8', 'jabKEhOmbZ4', 'dGZb1kv5zW0', 'ALQ7MLtEwtI', 'J2Bh68GTUOU', 'jq69R33z4hU', 'OXOj4bUuzSg', '7KKVb0_IdD4', 'ZN7DcixuLw4', 'ELZYwzTPUw4', 'Opq9QfaJp5I', 'WRSeV_27z6k', '7N74i_rAfFE', 'uovUU6FiI4E', '8rBadU7PmTs', '2AQxqxtAhNI', 'ZTmF2v59CtI', '_uUdJalMaF8', 'MAPPChRYp4k', 'x_NoA_Fp2Rc', 'C805Nt0JPIY', '1hM2AyOBD-o', 'E8zOp4Kqcls', 'yR5B-00peGQ', 'OUhrP5XtU_4', 'Wd2B8OAotU8', 'IsPOtygII-Q', 'JGmfGcOZUo4', 'uFnOk5cft48', 'qFkNATtc3mc', 'fV4x7OCqFLA', 'hJBHSmyqv0Y', '4h1WFyOQv0Y', '2Sycf4NUJ7s', 'SAQ74fZp2Ts', 'u6zDR5iVoTE', 'FDzYegv8JHE', 'OLEFphZ5Pm0', 'c769V25pX08', 'iXFTYhpDmB0', 'IFYJNLZT_B0', 'djDLB6k7ckM', 'ONEBmTZJ9xA', 'gcVbtUGLDNk', 'CiyAA_xraSo', 'CGLofayJvLQ', '-m9IGI5EgyM', 'cmMiyZaSELo', '_KoZ8khWf18', 'bSAlE_WgHxY', 'F_jIFDLu30Y', 'RzgezQh6900', 'm1rcse8INWk', 'X0tjzBfIHuI', '_WQCvtLTsfg', 'n3gPKbHeaQg', '2YoGxa1GH_8', 'kNaXjvKPiS0', 'Y7G-tYRzwYY', 'H9pv_BZ2PGA', 'R5CxtjmrIE4', 'XtqDTkvMJV8', 'b4b1cMVZOUU', 'Qh6WtwfMPdQ', 'MzhsLzOTZNA', 'Cc_cNEjAh_Y', 'P0KasU0HXD0', 'CtABUndA7tU', 'xQMMBANbcdQ', 'pElk1ShPrcE', 'lyWHtKq1PcQ', 'ruEQPQX90fI', 'oAVhUAaVCVQ', 'PIyf0hMc498', 'zC3UbTf4qrM', 'QwnJJXyrZhw', 'RDIRaFGr19s', 'P3_oXXtYx7s', 'xM_GfQvb36U', 'UW8a0WLbT0M', 'IXk1BQZ_rww', 'PZTErLrqJfw', 'gXe-KWe-YMs', '9LtJYw1eY30', 'rW9_-dVCmrM', 'IlsPKUrTAwM', '07UjanoLq_g', '16aQVvmFP7k', 'qiTtnlDPkBg', '0akqVN4ts0w', 'qcucgNV7Cmc', 'm66aEQ3Ssdw', 'WG6qKDoidmg', 'w5iA5LIwF2A', 'xyngwCXoMdI', '37ciobbzY3Q', 'huWzhZrazTk', 'QDKr7KHdgRU', 'GErvkyPzqpg', '24t-YFNDJwE', 'CReu_oE4sGc', 'WCoj11SzdPc', 'mS9J-a5W1Xc', '91F3hdi2Phc', 'yN21C972fsE', 'Qx8ShiEImYU', 'gVqfezvGvN4', 'lmPfioaW1Tw', 'AzWsY9hvB_8', 'xteZNX3B4yA', '84TjXsRHf6Q', 'ajYgbQWpBUU', 'UuLNftlHk8k', 'eALX-jZeUnI', 'T3CFfx2VIQY', 'ndYVtp6-spM', 'jDErhADhhmg', 'aPHsp9X2mBE', '8ZPhtWRtntU', 'uyBS_vaVH4U', 'Vkcki2dRCxM', 'aV32gcY9TaY', 'oOaboq4JQ4Q', 'ifT-NS_E7EY', '70QpN7DvaK4', 'Yx7KURxk5AQ', '15l6D9BK_D4', '7oqyfTpHmZE', 'zE7Pwgl6sLA', 'JJjdHWtQQk8', 'yDv0WSgXJVg', 'ZEMsTk5SPSg', 'ksY3wb4vtlA', 'o_Z4s7w2pQU', 'GL49u_5rYPM', '5Eqb_-j3FDA', '3N3n23loy24', '_V6_JsqWG0o', 'yHWPO9DDnsk', '-FP2Cmc7zj4', '5U5Ru0nTiUM', 'mrdRHsIkK_c', 'aNcxgxHcGYg', 'hsTQKwZEMQE', 'SAiyopkF22M', '9tYngcASnTA', 'Zhso97B4Rh4', 'Cu3QpWEfqgg', 'dbdtBQ16CXc', 'KT7oxGZmdv4', 'YYn8d1HYJoI', 'Ps-J0qGqg6Y', '7nDKFPWbJMU', 'uCMYzolEbO0', 'zns53qYaQIo', 'OdovkDUrC9Y', 'klYmPCjFLbM', 'pmHnlBqjpm0', 'jBpRItrod-Q', 'N7SgRFda9FU', 'MgbIwkzyW94', 'vvLBXO94EfA', 'vJQMhj6WYZA', 'T4tedh_11hg', 'f7qrT-Vd-C4', '3BsFE3WD0kA', 'bOipE-KvuBQ', 'RoaBANAPmRk', '-xIh-PDnaSw', 's5geihsSVM0', 'XaMfRN0PVQ8', 'jCEdTq3j-0U', '9a4izd3Rvdw', 'mK-XfCnttkE', '16e78n5x5mE', 'e1edxTqJnKk', 'Sut_KOIbwn0', '5IY4BNj0-10', 'L7TU0OH5lAw', 'dOR-yZgo1_0', 'di4Ggocqpb0', 'yidaL9xDlk8', 'lUFitnpPihs', 'qoq8B8ThgEM', 'uc43tD6-E4U', 'kdTleTWOeL4', 'A-dQUZowYHQ', 'IlVjro3FlXM', 'DpFUAyEnMeg', 'UdttyYOdUXU', 'eN6eDuKKDTQ', '1jf5kuvScJc', '87eSxDEO5oU', 'XvUSsh3gdO4', 'swcCuuQKGJ4', 'gSAcPWuXBOY', '7z3YeFqd7xQ', 'eGy-zA2HFvM', 'goPn5HAsNZo', '8HDTS80dlr4', 'DbiRVNeZPnw', 'D1G_jrSSEe4', 'T94PHkuydcw', '3mpx7oiZ_tM', 'yyYpmJx8zuU', '6hjJZv_68vI', 'KgmeL_xuB0I', '6ztQ92WSr7o', 'YPpOqfIQ5ME', 'dSD8XZVBO1M', 'Ykul19iM89Y', 'jG_7w2oSJpI', 'Y58g6UdRwJE', 'mocKoIhNJxk', 'FhDl8W0cBls', 'TNF7qxOmN9Y', 'Itntw6h2yEA', '5XjpV9n25Yk', 'h5u_MU50d6k', 'IBvg3WeqP1U', 'Q81ymh8vl4Q', '5OwOoQzLOyc', 'rHVB-w1Dt2g', '0Qs-Suk42dY', '80zh6tgMjtA', '8p5p2uTtDho', 'eM8Mjuq4MwQ', 'SpADOEqOMX0', 'Ezsb5afVXQQ', 'AI9p7boCO2I', 'w74c6Wnsz8g', 'ye9GqoslCKs', 'b-COwruFUyY', 'TLEPzT8jrUU', 'kL3ngGSf73A', 'i0BURncJM9Q', 'DCFrCX4HPO8', 'Gf7cE6NuZd4', 'hjfzFVw2Zjo', 'U2V0TgWHrR0', '1Na8nKEUjYI', 'Z3m0eWcP8n8', 'fxfezWYW39M', '9rvq0qVmNeQ', 'uBgJ0J2vtRk', '4YbAaRFk70o', 'pGuc4hPhiKw', 'WjAPDofGg28', 'L7TU0OH5lAw', 'SGFXdO-AjU0', 'jXlNjZnnCgc', 'Grr0FlC8SQA', 'fAzO3s7Dgnw', 'T-g39o0rDos', 'ecPMVO7JuTo', 'vjK02kjgDws', 'aGbPyM6lzBs', 'jitmi9o3As8', 'BoySkwX90mM', '6DKja1WRJ1k', '1Z_cClBsABE', 'fqjXS7X9_5s', 'T15qhmhqraE', 'dx4Teh-nv3A', '3u6lLWGjFLY', 'CHwlXtF3zXs', 'uUPBMV3DAck', 'sJ93P9YMnro', 'dovWTFlRIWs', 'YFvkvQxkg5A', 'TaVQDO1Xk7M', 'P1ZwWKcPV5Y', 'w3MMMgxjLFk', 'LEYXdZ_rVbo', 'AKF2whlGnr4', 'yWeVII7qF3A', 'ME7yIky1pgI', 'D21Di3NXcYM', 'k7_SG8aDleI', 'VKdseOYqtOE', 'yXads67NX9A', 'vr8RaNuWjWc', '7CGRrgP8U3c', 'NapGAjs2nXE', 'fwtCkbRTFgw', 'IWZFRzF_ndg', 'dOR-yZgo1_0', 'WeY9hdsmIaQ', 'sm2hNJ9c8M8', '5WB8ujhAK7c', 'VwAAtZp3XZ8', 'wdxebKzUfIM', 'Xf1922kJPfU', '8iQU0ubwVdY', 'UKQ0BuFErq4', '_9geEbZIAJM', 'e3EZ2YRoihU', 'FouthqX6640', 'fcssf-Wwbv4', 'AK2upOdOtek', 'Ujb2c508yw0', '8Z8qobg8UdA', '0AqZzax9_Og', 'y5kzKWu9cas', 'rxMmistOjCA', 'kuZ1hSfDrS4', 'NobzfIebbrE', 'c2gSzYLJ8sY', 'VlbGL4mCksI', 'zV7pfxeh5dY', '5lf_Ujt0BXo', 'Hd4l4q1hfps', 'Jtg2zyS_y_c', 'V8zXLMIjlcw', 'TyMUY2CDrjc', 'jH4_GTRUC14', 'xARHpBzxFNI', 'PzcSrkMKDdk', '_HqrjLxKtKM', 'N9IGKvBgTO8', 'dv_Qjzca56k', 'NrGrb0Annlk', '1iJf_8E7f8c', 'NbWKYgaWzbI', 'q3Ui0ETENUU', 'pmHnlBqjpm0', 'dBUxfFoQpuo', 'GUBa1wRxQko', 'lkyZrD_SNAI']
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