# 🎬 Streaming Availability Finder

A Streamlit web app to search for movies and series, view their overviews, posters, and find out where you can stream them, powered by the [Streaming Availability API](https://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability).

## Access here

Here is the [link](https://movie-find.streamlit.app/) for checking out the app

## 🚀 Features

- Search for movies or series by title
- Choose country and content type (movie/series)
- View overview, original title, release year, and poster
- Get direct streaming links for each result

## 🛠️ Setup & Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/ankit85810/streaming-availability-finder.git
    cd streaming-availability-finder
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Add your API key:**

    - **Locally for testing:**  
      Create a file at `.streamlit/secrets.toml` with the following content:
      ```
      api_key = "YOUR_RAPIDAPI_KEY"
      ```
    - **On Streamlit Cloud:**  
      Add your API key in the app’s **Secrets** section as:
      ```
      api_key = "YOUR_RAPIDAPI_KEY"
      ```

4. **Run the app:**
    ```
    streamlit run main.py
    ```

## 🌐 Deployment

- Deploy easily to [Streamlit Cloud](https://streamlit.io/cloud) by connecting your GitHub repo.
- Add your API key in the app’s **Secrets** section after deployment for secure access.

## 📁 Project Structure

.
├── main.py           # Streamlit app UI
├── server.py         # API logic and data fetching
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── .streamlit/
    └── secrets.toml  # (Not committed) API keys and secrets

## ⚠️ Important Security Note

**Never commit your API key to GitHub.**  
Always use `.streamlit/secrets.toml` (locally) or Streamlit Cloud Secrets (when deployed).


---

*Made with ❤️ using Streamlit and the Streaming Availability API*
