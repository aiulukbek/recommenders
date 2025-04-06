from typing import List 
from utils.predictor import Predictor
class Metric: 
    def __init__(self, predictor : Predictor): 
        self.predictor = predictor 
        self.vocabulary = self.predictor.get_vocabulary() 

    def _intersection(self, preds : List, actual : List) -> int: 
        return len(set(preds) & set(actual))

    def hit_rate(self, preds: List, actual : List)-> float: 
        return int(self._intersection(preds, actual) > 0) 
    
    def precision(self, preds : List, actual : List) -> float: 
        return self._intersection(preds, actual) / len(preds) 
    
    def recall(self, preds : List, actual : List) -> float: 
        return self._intersection(preds, actual) / len(actual) 

    def calculate(self, seq : List, func : str, k = 10) -> float:
        if hasattr(self, func): 
            metric_func = getattr(self, func)
        else: 
            raise KeyError(f'Method with name {func} is not defined.')
        values = []
        for _ in range(len(seq)): 
            item = seq.pop(0) 
            if item in self.vocabulary:
                recos = self.predictor.get_recommendations(item) 
                recos = recos[:k]
                value = metric_func(recos, seq) 
                values.append(value)
            seq.append(item)
        return sum(values) / len(values)  if len(values) > 0 else 0
    
    
    