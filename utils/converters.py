
# helper functions for formatting and date conversions 
import numpy as np 
import pandas as pd 
from typing import List 


def convert_to_list(items : List[np.int64]) -> List[int]: 
    """
        converts list of numpy into list of ints 
        Params:
            :param items - the sequence of numpy arrays 
        Returns: 
            a list of integers 
    """
    new_items = [item.item() for item in items] 
    return new_items 


def timestamp_to_datetime(timestamp: pd.Series ) -> pd.Timestamp: 
    """
        converts unixtimestamp into datetime 
        Params: 
            :param timestamp - unixtimestamp 
        Returns: 
            datetime 
    """
    try:
        timestamp_date = pd.to_datetime(timestamp, unit = 'ms')
    except Exception as e: 
        print("Unable to convert to datetime from {timestamp} to datetime : error({e})")
        return None
    return timestamp_date

def datetime_to_date(dt: pd.Series) -> pd.Series: 
    """
        converts datetime into date 
        Params: 
            :param dt - datetime 
        Returns: 
            a series in date format 
    """
    values = np.all(dt.apply(lambda item: isinstance(item, pd.Timestamp)).values)

    if not values:
        raise TypeError("dt has to be in format timestamp.")
    return dt.dt.date

def format_date(events : pd.DataFrame) -> pd.DataFrame: 
    """
        formats event timestamp into proper date formats 
        Params: 
            :param events - events dataframe 
        Returns: 
            events with proper date formats 
    """
    events['event_datetime'] = timestamp_to_datetime(events.timestamp)
    events['events_date'] = datetime_to_date(events.event_datetime)
    return events