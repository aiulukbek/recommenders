import pytest 
from pathlib import Path 
from utils.predictor import Predictor
from utils.metric import Metric


@pytest.fixture 
def get_actual_pred_data_with_full_intersection(): 
    actual = [1,2,3,4,5]
    pred = [1,2,3,4,5]
    return actual, pred 

@pytest.fixture 
def get_actual_pred_data_with_zero_intersection(): 
    actual = [1,2,3,4,5]
    pred = [6,7,8,9,10]
    return actual, pred 

@pytest.fixture 
def get_actual_pred_data_with_half_intersection(): 
    actual = [1,2,3,4,5,6] 
    pred = [1,2,3, 7, 8, 9] 
    return actual, pred

@pytest.fixture
def get_actual_half_pred_data_intersection(): 
    actual = [1,2,3, 4, 5, 6] 
    pred = [1,2,3, 7, 8, 9]
    return actual, pred 

@pytest.fixture
def get_metric(): 
    model_path = Path("model/embedding_model.model")
    predictor = Predictor(model_path)   
    metric = Metric(predictor=predictor)
    return metric 
    
def test_hitrate(get_actual_pred_data_with_full_intersection, 
                 get_metric): 
    metric = get_metric
    actual, pred = get_actual_pred_data_with_full_intersection
    value = metric.hit_rate(pred, actual)
    assert value > 0 , "Hit rate has to be 1. "


def test_hitrate_with_zero_intersection(get_actual_pred_data_with_zero_intersection, get_metric): 
    metric = get_metric 
    actual, pred = get_actual_pred_data_with_zero_intersection 
    value = metric.hit_rate(pred, actual) 
    assert value == 0, "Hiot rate has to be 0."

def test_precision_with_half_intersection(get_actual_pred_data_with_half_intersection, get_metric): 
    actual, pred = get_actual_pred_data_with_half_intersection
    metric = get_metric 
    value = metric.precision(pred, actual)
    assert value == 0.5 , "Precision has to be 0.5" 

def test_recall_with_half_intersection(get_actual_half_pred_data_intersection, get_metric): 
    actual, pred = get_actual_half_pred_data_intersection 
    metric = get_metric 
    value = metric.recall(pred, actual) 
    assert value == 0.5, "Recall has to be 0.5" 



