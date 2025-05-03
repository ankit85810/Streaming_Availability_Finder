import streamlit as st
import server as sr

st.set_page_config(page_title="Streaming Search", layout="wide")

st.title("🎬 Streaming Availability Finder")

# --- Step 1: Select Country ---
countries = {
    "Canada": "ca", "USA": "us", "Brazil": "br", "UK": "gb",
    "Germany": "de", "South Africa": "za", "India": "in", "Japan": "jp"
}
country = st.selectbox("🌍 Choose a Country", list(countries.keys()))
country_code = countries[country]

# --- Step 2: Select Type (Movie/Series) ---
show_type = st.radio("🎞️ Select Type", ["Movie", "Series"])
show_type_api = show_type.lower()

# --- Step 3: Enter Name of Movie/Series ---
search_query = st.text_input(f"🔎 Enter {show_type} Name")

# --- Step 4: Submit Button ---
if st.button("Search"):
    if not search_query.strip():
        st.warning("Please enter a name to search.")
    else:
        st.info("Fetching results...")

        # Fetch data
        overviews = sr.get_overview(title=search_query, country=country_code, show_type=show_type_api)
        posters = sr.get_posters(title=search_query, country=country_code, show_type=show_type_api)
        links = sr.get_links(title=search_query, country=country_code, show_type=show_type_api)

        if isinstance(overviews, str):
            st.error(overviews)
        elif not overviews:
            st.warning("No results found.")
        else:
            for idx, overview in enumerate(overviews):
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.subheader(f"{overview['title']} ({overview['release_year']})")
                    st.markdown(f"**Original Title:** {overview['original_title']}")
                    st.markdown(f"**Country:** {country}")
                    st.markdown("**Overview:**")
                    st.write(overview["overview"] or "No overview available.")

                    # Show streaming links if available
                    show_links = links[idx] if idx < len(links) else []
                    if show_links:
                        st.markdown("**Available On:**")
                        for link in show_links:
                            st.markdown(f"- [{link['name']}]({link['link']})")
                    else:
                        st.info("No streaming links available for this title.")

                with col2:
                    poster_url = posters[idx] if idx < len(posters) else None
                    if poster_url:
                        st.image(poster_url, use_column_width=True)
                    else:
                        st.warning("Poster not available.")
                st.markdown("---")
