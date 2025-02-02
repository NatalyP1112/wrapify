"""
config.py

Holds configuration constants (Spotify credentials, Redirect URI, etc.).
"""

# Replace these with your actual Spotify Developer credentials
SPOTIFY_CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_SPOTIFY_CLIENT_SECRET"
SPOTIFY_REDIRECT_URI = "YOUR_SPOTIFY_REDIRECT_URI" # this is the URL to which Spotify will send the user back (after login)

# Scope depending on what data is retrieved
# lists which permissions we're requesting from the user:
#   user-top-read: allows the app to see the user's top tracks/artists.
#   user-read-recently-played: allows seeing recently played tracks.
SCOPES = [
    "user-top-read", 
    "user-read-recently-played"
    # Feel free to add more :)
]
