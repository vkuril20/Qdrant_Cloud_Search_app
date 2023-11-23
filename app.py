import streamlit as st
import requests
import pandas as pd
import time

# Set the URL for the backend service (FastAPI server)
api_url = "http://127.0.0.1:8000/api/search"

# Class for a Streamlit web app focused on searching products
class ProductFinder:
    def __init__(self, api_endpoint):
        # Initialize with the API endpoint
        self.api_endpoint = api_endpoint
        self.welcome_message = "Search for product information in our database"

    def launch(self):
        # Constructing the Streamlit interface
        st.header("BigBasket Product Finder")
        st.caption(self.welcome_message)

        # Input fields for user query and additional feedback
        user_query = st.text_input("Search for a product:")
        feedback_box = st.sidebar.text_area("Feedback or Suggestions")

        # Initiating search on button click
        if st.button("Start Search"):
            self.initiate_search(user_query)

    def initiate_search(self, query):
        # Requesting data from the backend using the provided query
        search_response = requests.get(f"{self.api_endpoint}/?q={query}")

        # Displaying a progress bar during data retrieval
        progress = st.progress(0)
        for completion in range(100):
            time.sleep(0.01)  # Mimicking a loading process
            progress.progress(completion + 1)

        # Handling the response from the backend
        if search_response.status_code == 200:
            progress.empty()  # Hide the progress bar after completion
            self.show_results(search_response)
        else:
            st.error(f"Failed to retrieve data: {search_response.status_code} - {search_response.text}")

    def show_results(self, api_response):
        # Processing and displaying the results from the API
        search_results = api_response.json()["result"]
        result_dataframe = pd.DataFrame(search_results)
        
        st.subheader("Search Results:")
        st.dataframe(result_dataframe)

# Entry point for the Streamlit application
if __name__ == "__main__":
    # Instantiate and run the ProductFinder application
    finder_app = ProductFinder(api_url)
    finder_app.launch()
