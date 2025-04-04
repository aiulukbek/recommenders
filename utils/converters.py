
import numpy as np 
from typing import List 

def convert_to_list(items : List[np.int64]) -> List[int]: 
    new_items = [item.item() for item in items] 
    return new_items 