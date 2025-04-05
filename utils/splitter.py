import datetime 
import pandas as pd 
from typing import Tuple 
from typing import List
from configs.split_configs import get_split_configs

def train_test_split(split_point : str, events : pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]: 
    split_date = datetime.datetime.strptime(split_point, "%Y%m%d").date() 
    train_set = events[events.events_date < split_date] 
    test_set =  events[events.events_date >= split_date] 
    return train_set, test_set



def get_sequences(events: pd.DataFrame) -> List[List]: 
    conf_split = get_split_configs() 
    group_keys = conf_split['group_keys']
    sequence_key = conf_split['sequence_key']
    return events.groupby(group_keys)[sequence_key].apply(list).reset_index()[sequence_key].tolist() 

