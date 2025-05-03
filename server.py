import requests
import streamlit as st

API_URL = "https://streaming-availability.p.rapidapi.com/shows/search/title"
api_key = st.secrets["api_key"]

HEADERS = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "streaming-availability.p.rapidapi.com"
}


def get_overview(title, country="in", show_type="movie"):
    """
    Fetches overview information for a title.
    Returns a list of dicts with title, overview, release_year, and original_title.
    """
    params = {
        "country": country,
        "title": title,
        "series_granularity": "show",
        "show_type": show_type,
        "output_language": "en"
    }
    response = requests.get(API_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        data = response.json()
        return [
            {
                "title": item.get("title"),
                "overview": item.get("overview"),
                "release_year": item.get("releaseYear"),
                "original_title": item.get("originalTitle")
            }
            for item in data
        ]
    return response.json().get("message", "Unknown error")


def get_posters(title, country="in", show_type="movie"):
    """
    Fetches poster URLs for a title.
    Returns a list of poster image URLs.
    """
    params = {
        "country": country,
        "title": title,
        "series_granularity": "show",
        "show_type": show_type,
        "output_language": "en"
    }
    response = requests.get(API_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        data = response.json()
        return [
            item.get("imageSet", {}).get("verticalPoster", {}).get("w480")
            for item in data
        ]
    return response.json().get("message", "Unknown error")


def get_links(title, country="in", show_type="movie"):
    """
    Fetches streaming links for a title.
    Returns a list of lists of dicts with service name and link.
    """
    params = {
        "country": country,
        "title": title,
        "series_granularity": "show",
        "show_type": show_type,
        "output_language": "en"
    }
    response = requests.get(API_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        data = response.json()
        links = []
        for item in data:
            show_links = []
            try:
                for link_item in item["streamingOptions"].get(country, []):
                    show_links.append({
                        "name": link_item["service"]["name"],
                        "link": link_item["link"]
                    })
            except (KeyError, TypeError):
                pass  # No streaming links for this show in this country
            links.append(show_links)
        return links
    return response.json().get("message", "Unknown error")
