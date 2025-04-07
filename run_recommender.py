import argparse 
import logging 
import pandas as pd 
import numpy as np 
from pathlib import Path 
from utils.readers import CSVReader
from utils.converters import format_date
from utils.splitter import train_test_split
from utils.splitter import get_sequences
from configs.split_configs import get_split_configs
from configs.artifact_configs import get_artifact_configs
from configs.model_configs import get_model_params
from utils.trainer import Trainer
from utils.predictor import Predictor
from utils.metric import Metric

# logger is added 
logger = logging.getLogger(__name__) 
logging.basicConfig(level = logging.INFO)

def format_dataset(): 
    configs = get_artifact_configs()
    dirname = Path(configs['data_folder']) 
    filename = Path(configs['dataset']) 
    file_path = dirname / filename 
    logging.info(f"Path to events : {file_path}")
    events = CSVReader.read(str(file_path))
    events = format_date(events=events)
    logging.info(f"events: {events.shape}")
    return events 

def filter_sequences(sequences): 
    sequences_filtered = [list(seq) for seq in sequences if len(seq) > 1 and len(seq) < 20]
    return sequences_filtered

def get_train_test_sets(events): 
    split_point = get_split_configs()['split_point']
    train_set, test_set = train_test_split(split_point=split_point, events=events)
    train_sequences = get_sequences(train_set)
    test_sequences = get_sequences(test_set)
    return train_sequences, test_sequences

def save(trainer): 
    configs = get_artifact_configs() 
    path_to_save = Path(configs['model_folder']) 
    filename = path_to_save / Path(configs['model_name'])
    trainer.save(str(filename))

def calculate_metrics(test_sequences_filtered):
    configs = get_artifact_configs()
    model_path = Path(f"{configs['model_folder']}/{configs['model_name']}")
    predictor = Predictor(model_path)
    metric = Metric(predictor=predictor)
    # let us take sample of test datasets 
    sample = test_sequences_filtered[: 1000] 
    precision_10 = np.mean([metric.calculate(seq, 'precision') for seq in sample]) 
    recall_10 = np.mean([metric.calculate(seq, 'recall') for seq in sample])
    hitrate_10 = np.mean([metric.calculate(seq, 'hit_rate') for seq in sample])
    return precision_10, recall_10, hitrate_10 

def model_training(): 
    events = format_dataset() 
    train_sequences, test_sequences = get_train_test_sets(events) 
    train_sequences_filtered = filter_sequences(train_sequences)
    test_sequences_filtered = filter_sequences(test_sequences)
    params = get_model_params() 
    trainer = Trainer(train_sequences_filtered, params)
    trainer.train()
    save(trainer=trainer)
    precision_10, recall_10, hitrate_10 = calculate_metrics(test_sequences_filtered)
    logging.info(f"precision: {precision_10} recall: {recall_10} hirtate: {hitrate_10}")
    
def make_recommendations(itemid): 
    configs = get_artifact_configs() 
    model_path = Path(f"{configs['model_folder']}/{configs['model_name']}")
    predictor = Predictor(model_path)
    recos = predictor.get_recommendations(itemid)
    return recos 

def run(args): 
    is_training  = args.is_training
    if is_training: 
        logging.info("Training is started.")
        model_training()
    else: 
        itemid = args.itemid
        recos = make_recommendations(itemid)
        logging.info(f"Recommendations for {itemid} is {recos}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--is_training", 
        default=False, 
        type = bool, 
        help="Whether to train or predict"
    ) 

    parser.add_argument(
        '--itemid', 
        default = -1, 
        type = int, 
        help = "Item id for recommendation."
    )

    args : argparse.Namespace = parser.parse_args() 
    run(args=args)

