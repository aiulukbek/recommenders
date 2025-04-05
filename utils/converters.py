
import numpy as np 
import pandas as pd 
from typing import List 


def convert_to_list(items : List[np.int64]) -> List[int]: 
    new_items = [item.item() for item in items] 
    return new_items 


def timestamp_to_datetime(timestamp: pd.Series ) -> pd.Timestamp: 
    try:
        timestamp_date = pd.to_datetime(timestamp, unit = 'ms')
    except Exception as e: 
        print("Unable to convert to datetime from {timestamp} to datetime : error({e})")
        return None
    return timestamp_date

def datetime_to_date(dt: pd.Series) -> pd.Series: 
    values = np.all(dt.apply(lambda item: isinstance(item, pd.Timestamp)).values)

    if not values:
        raise TypeError("dt has to be in format timestamp.")
    return dt.dt.date

def format_date(events : pd.DataFrame) -> pd.DataFrame: 
    events['event_datetime'] = timestamp_to_datetime(events.timestamp)
    events['events_date'] = datetime_to_date(events.event_datetime)
    return events