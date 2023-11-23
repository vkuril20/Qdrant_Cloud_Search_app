from fastapi import FastAPI
from neural_searcher import NeuralSearcher
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Create a FastAPI application instance
app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing) for all routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Initialize the NeuralSearcher with the specified collection_name
query_searcher = NeuralSearcher(collection_name='bigbasket_vectors')


# Define a route to handle search requests
@app.get("/")
def search_startup(q: str):
    """
    Handle search requests.

    Parameters:
    - q (str): The search query.

    Returns:
    - dict: A dictionary containing the search result.
    """
    return {
        "result": query_searcher.search(text=q)
    }


if __name__ == "__main__":
    # Run the FastAPI application using Uvicorn with specified host and port
    uvicorn.run(app, host="0.0.0.0", port=8000)