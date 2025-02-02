"""
views.py

Django views for displaying Spotify data in a web interface.
"""

import os
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from authentication import get_spotipy_client
from data_processing import process_top_tracks, process_top_artists
from spotify_data import get_top_tracks, get_top_artists


# HOME PAGE
def index(request: HttpRequest) -> HttpResponse:
    """
    Renders the home page. If user is authenticated with Spotify,
    displays top tracks/artists. Otherwise, shows a 'login with Spotify' link.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page.
    """
    # Check if we have an access token in session or local token cache
    token_info = _get_token_from_cache()
    if not token_info:
        # No token: Show link to Spotify login
        return render(request, 'wrapify/index.html', {"authenticated": False})

    # If we have a token, create a spotipy client using it
    sp = get_spotipy_client(cache_path=".spotipyoauthcache")
    
    # Fetch user's display name
    user_profile = sp.current_user()
    user_name = user_profile.get("display_name", "Spotify User")
    
    # Fetch data
    raw_tracks = get_top_tracks(sp)
    raw_artists = get_top_artists(sp)
    # Process data
    processed_tracks = process_top_tracks(raw_tracks)
    processed_artists = process_top_artists(raw_artists)

    context = {
        "authenticated": True,
        "user_name": user_name,
        "tracks": processed_tracks,
        "artists": processed_artists,
    }
    return render(request, 'wrapify/index.html', context)


# SPOTIFY OFFICIAL LOGIN PAGE (+ PERMISSIONS)
def spotify_login(request: HttpRequest) -> HttpResponse:
    """
    Redirects user to Spotify OAuth page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirect to the Spotify authorization URL.
    """
    sp_auth = get_spotipy_client(cache_path=".spotipyoauthcache").auth_manager
    auth_url = sp_auth.get_authorize_url()
    return redirect(auth_url)


# LOGIN PAGE -> HOME PAGE
def spotify_callback(request: HttpRequest) -> HttpResponse:
    """
    Handles the Spotify redirect/callback. Completes OAuth flow.

    Args:
        request (HttpRequest): The HTTP request object containing 'code' from Spotify.

    Returns:
        HttpResponse: Redirect to home.
    """
    code = request.GET.get('code') # a temporary authorization code used to securely exchange for an access token
    error = request.GET.get('error')
    if error:
        return HttpResponse(f"Error from Spotify: {error}")

    sp_auth = get_spotipy_client(cache_path=".spotipyoauthcache").auth_manager
    # This will fetch the token using the 'code'
    sp_auth.get_access_token(code)
    # You could store token_info in the Django session or rely on the .spotipyoauthcache file !!!!!!!!!!!!!!!!!!!!!!!!!!!!
    return redirect('index')

def logout_view(request: HttpRequest) -> HttpResponse:
    """
    Clears the Spotipy token cache and redirects the user to the index page.
    """
    if os.path.exists(".spotipyoauthcache"):
        os.remove(".spotipyoauthcache")
    return redirect('index')

def _get_token_from_cache() -> bool:
    """
    Helper function to check if .spotipyoauthcache file exists
    and has valid tokens.

    Returns:
        bool: True if token file exists, False if not.
    """
    return os.path.exists(".spotipyoauthcache")
