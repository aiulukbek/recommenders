from ml_collections import config_dict 


def get_artifact_configs(): 
    configs = config_dict.ConfigDict()
    configs.data_folder = "data" 
    configs.model_folder = "model" 
    configs.model_name = "embedding_model.model" 
    configs.dataset = "events.csv"
    return configs
    