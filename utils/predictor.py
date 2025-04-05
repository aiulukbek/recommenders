import os 
from gensim.models import Word2Vec
from pathlib import Path 
from typing import List 
class Predictor: 
    def __init__(self, path : Path):
        self.model_path = str(path) 
        self._load_model()
        self._load_embeddings()
        self._load_vocabulary()


    def _load_model(self) -> Word2Vec: 
        self._check_path(self.model_path)
        self.model = Word2Vec.load(self.model_path) 

    def _load_embeddings(self): 
        self._check_model() 
        self.embeddings = self.model.wv

    def _load_vocabulary(self): 
        self._check_model() 
        self.vocabulary = self.model.wv.index_to_key

    def get_recommendations(self, itemid: str) -> List: 
        self._check_key(itemid) 
        recos = self.model.wv.most_similar(itemid) 
        recos = [reco[0] for reco in recos]
        return recos
    
    def get_embedding(self, itemid: str): 
        self._check_key(itemid) 
        embedding = self.embeddings[itemid]
        return embedding
    

    def _check_model(self): 
        if not self.model:
            raise ValueError("Model is not defined.")
    
    def _check_key(self, key: str): 
        self._check_model() 
        if key not in self.model.wv: 
            raise KeyError(f"Key {key} is not found.")
        
    def _check_path(self, path: str):
        if not os.path.isfile(path): 
            raise FileNotFoundError("Model is not found.") 

        