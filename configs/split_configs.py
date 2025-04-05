from ml_collections import config_dict 


def get_split_configs(): 
    split_config = config_dict.ConfigDict() 
    split_config.split_point = "20150801"
    split_config.group_keys = ['events_date', 'visitorid']
    split_config.sequence_key = "itemid"
    return split_config
