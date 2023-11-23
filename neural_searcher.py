import qdrant_client
import os
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
os.environ['QDRANT_HOST'] ="YOUR_QDRANT_HOST_URL"
os.environ['QDRANT_API_KEY'] ="YOUR_QDRANT_API_KEY"
COLLECTION_NAME="bigbasket_vectors"
vector_field_name="bigbasket_vectors_field"

# https://qdrant.tech/documentation/concepts/filtering/
class NeuralSearcher:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
        self.qdrant_client = QdrantClient(os.getenv("QDRANT_HOST"),
        api_key=os.getenv("QDRANT_API_KEY"))

    def search(self, text: str):
        vector = self.model.encode(text).tolist()

        hits = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=(vector_field_name,vector),
            query_filter=None,  
            limit=7  
        )
        
        result = [hit.payload for hit in hits]
        return result
    

    