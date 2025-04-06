# A module implements model prediction 
import os 
from gensim.models import Word2Vec
from typing import List 
from pathlib import Path 
class Predictor: 
    """
        Model prediction 
        Params: 
            :param path - a path for trained model 
    """
    def __init__(self, path : Path):
        self.model_path = str(path) 
        self._load_model()
        self._load_embeddings()
        self._load_vocabulary()


    def _load_model(self) -> Word2Vec: 
        """
            loads a trained model 
        """
        self._check_path(self.model_path)
        self.model = Word2Vec.load(self.model_path) 

    def _load_embeddings(self): 
        """
            loads embeddings 
        """
        self._check_model() 
        self.embeddings = self.model.wv

    def _load_vocabulary(self): 
        """
            loads vocabulary
        """
        self._check_model() 
        self.vocabulary = self.model.wv.index_to_key

    def get_recommendations(self, itemid: str) -> List: 
        """
            generates recommendations for the given item 
            Params: 
                :param itemid- unique identifier of the product 
            Returns: 
                - recommendations for the given item 
        """
        self._check_key(itemid) 
        recos = self.model.wv.most_similar(itemid) 
        recos = [reco[0] for reco in recos]
        return recos
    
    def get_embedding(self, itemid: str): 
        """
            generates embeddings for the given item 
            Params: 
                :param itemid - unique identifier of the product 
            Returns: 
                embedding of the product 
        """
        self._check_key(itemid) 
        embedding = self.embeddings[itemid]
        return embedding
    
    def get_vocabulary(self)-> List: 
        """ 
            returns vocabulary from the trained model 
        """
        return self.vocabulary
    

    def _check_model(self): 
        """
            checks whether a model is trained 
        """
        if not self.model:
            raise ValueError("Model is not defined.")
    
    def _check_key(self, key: str): 
        """
            checks whether a key exists 
        """
        self._check_model() 
        if key not in self.model.wv: 
            raise KeyError(f"Key {key} is not found.")
        
    def _check_path(self, path: str):
        """
            checks whether file exists 
        """
        if not os.path.isfile(path): 
            raise FileNotFoundError("Model is not found.") 

        