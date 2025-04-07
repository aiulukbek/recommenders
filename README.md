# RecSys
This repo for recommendation system using Embeddings  

Main goal is to recommend the most similar products depending on the sequences; 

Sequences contain products which corresponds to the following events: 
- view
- addtoart
- purchase

Word2Vec model is trained using sequence of items. 

Metrics : 
- precision@k
- recall@k
- hitrate@k

The definition of the metrics can be found in any literature related to recommendation systems, 
since they are standard metrics in any recommendation systems. 

Dataset: 

- retail dataset is used ;
- only behavior data is considered;

- link to the data : https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset/data 


Run: 
- is_training  = True to train the model , default = False 
- itemid unique identifier of product to generate recommendations, default = "" 


Example: 
  python run_recommender.py --is_training True -> to train a model 
  
  python run_recommender.py --is_training False --itemid {unique identifier}  -> to generate recommendations 
