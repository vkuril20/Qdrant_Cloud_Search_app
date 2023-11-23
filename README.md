# Query_Search_BigBasket
# with Qdrant + LLM + FastAPI + Streamlit
This repository contains a code for Query Search in [Bigbasket Products Dataset](https://chaabiv2.s3.ap-south-1.amazonaws.com/hiring/bigBasketProducts.csv) 
.
# Requirements
Before using this app , make sure you have the following:

* Python 3.x installed on your system.
* An active Qdrant Managed Cloud Service account.
* Your Qdrant Managed Cloud Service credentials.
  
Install the required Python packages using pip:  
```
pip install -r requirements.txt  
```
To perform search on the dataset you have to convert the given csv_dataset into vectors  
Code for initial data preparation could be found in [Colab Notebook](https://colab.research.google.com/drive/1Q2SPPmwlWGvq_VXBK0XSQqgFCza-Ulxq)  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Q2SPPmwlWGvq_VXBK0XSQqgFCza-Ulxq)  
After evaluating Colab you should get  encoded vectors in file ./data/vectors_bigbasket.npy
