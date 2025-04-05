from typing import Dict
from gensim.models import Word2Vec
class Trainer: 
    def __init__(self, training_set, params : Dict): 
        self.training_set = training_set 
        self.params = params 
        self.is_trained = False

    def train(self): 
        self.model = Word2Vec(**self.params) 
        self.model.build_vocab(self.training_set) 
        self.model.train(self.training_set, total_examples = self.model.corpus_count, epochs = self.model.epochs) 
        self.is_trained = True 

    def embeddings(self): 
        if not self.is_trained: 
            raise ValueError("Model is not trained yet.")
        
        if not self.embeddings and self.is_trained: 
            self._embeddings = self.model.wv

        return self._embeddings 
    
    def vocabulary(self): 
        if not self.is_trained: 
            raise ValueError("Model is not trained yet.")
        
        if not self._vocabulary and self.is_trained: 
            self._vocabulary = self.model.index_to_key
        
        
        return self._vocabulary
    

    def save(self, path : Path): 
        if not self.is_trained:
            raise ValueError("Model is not trainer yet.") 
        path_str = str(path)
        self.model.save(path_str) 

    def load(self, path : Path): 
        if not self.is_trained: 
            raise ValueError("Model is not trained yet.")
        
        path_str = str(path)
        self.model = Word2Vec.load(path_str)
    
        

        
        

        