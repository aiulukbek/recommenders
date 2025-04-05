from ml_collections import config_dict 


def get_model_params(): 
    model_params = config_dict.ConfigDict()
    model_params.epochs = 10
    model_params.ns_exponent = 0.75
    model_params.min_count = 1
    model_params.window = 20
    model_params.vector_size = 64 
    return model_params 