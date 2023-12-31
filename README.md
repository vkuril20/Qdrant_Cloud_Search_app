# Query_Search_BigBasket
# using Qdrant, LLM, FastAPI & Streamlit
This repository contains an Web app with a graphical user interface (GUI) that connects to a remote database hosted in Qdrant's Managed Cloud Service and answer Query Searches from [Bigbasket Products Dataset](https://chaabiv2.s3.ap-south-1.amazonaws.com/hiring/bigBasketProducts.csv) 

# Requirements
Before using this app , make sure you have the following:

* Python 3.x installed on your system.
* An active Qdrant Managed Cloud Service account.
* Your Qdrant Managed Cloud Service credentials.
* Qdranr cluster url.
* Qdrant cluster api_key.
  
Install the required Python packages using pip:  
```
pip install -r requirements.txt  
```
# Process Dataset & Implement Vector Embeddings
To perform search on the dataset you have to convert the given csv_dataset into vectors  
Code for initial vector preparation could be found in [Dataset_to_Vectors Collab Notebook](https://colab.research.google.com/drive/1Q2SPPmwlWGvq_VXBK0XSQqgFCza-Ulxq)  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Q2SPPmwlWGvq_VXBK0XSQqgFCza-Ulxq)  
After evaluating Colab you should get  encoded vectors in file ``` ./data/vectors_bigbasket.npy ``` 

# Upload Vector Embeddings & Implement LLM to answer contextual queries 
To Implement LLM on the Qdrant DB you have to upload the vector Embeddings downloaded from the [Dataset_to_Vectors Notebook](https://colab.research.google.com/drive/1Q2SPPmwlWGvq_VXBK0XSQqgFCza-Ulxq) into the Qdrant DB    

This collab notebook will require your Qdrant url and api_key.  
Create a qdrant_client collection and vector_field_name to store vector embeddings, these credentials will be further used.  

Code to upload vector embeddings & answering queries through LLM can be found in [Upload Vectors Collab Notebook](https://colab.research.google.com/drive/1dvZ7N8OtfN_gBZYDKPvTiG5sfLO4Y-eo)  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dvZ7N8OtfN_gBZYDKPvTiG5sfLO4Y-eo)  
Vector Embeddings are now uploaded to Qdrant DB   

# Create a Neural searcher to be used in FASTAPI which answer queries from the Qdrant DB  
make sure you create ```neural_Sercher.py``` in your env locally   
Replace the QDRANT_HOST_URL and QDRANT_API_KEY with your qdrant url and api_key, also replace the collection name and vector_field_name with the ones you created while uploading vector embeddings.

# Integrating with FastAPI   
To launch the Fast API service, execute the fastapi.py file in a separate terminal using the following command:  
```
uvicorn service:app 
```
After a successful upload, neural search API will be available at  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

# Launch the streamlit Web app  
This streamlit app uses FastAPI url as the backend api_key  
you can run the app using the following command:  
```
streamlit run app.py
```
This command will start the application.

  
# Here are some Search results:
* .
 ![Strawberry Ice Cream](Data/strawberry_ice_cream.png)

* .
 ![toothpaste](Data/toothpaste.png)
