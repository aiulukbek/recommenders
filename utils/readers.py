# data reading module: csv reader 

import pandas as pd 
from abc import ABC 
from abc import abstractmethod

class Reader(ABC): 
    """
      Parent class is responsible for data reading abstraction 
      Classes inheriting this class has to implement abstract method and their 
      corresponding logic 
    """
    @staticmethod
    @abstractmethod
    def read(file_name: str) -> pd.DataFrame:
        pass



import os 
class CSVReader(Reader): 
  """
    The class is responsible for reading csv files 
  """
  @staticmethod
  def read(file_name:str) -> pd.DataFrame: 
    """ 
      The method is responsible for reading csv file 

      Params: 
        :param file_name: name of a file to read 
      
      Returns: 
        :return: pandas dataframe 
    """ 
    if not isinstance(file_name, str):
      raise TypeError("file name must be string.")
    
    extension = file_name.split(".")[-1]
    if extension != "csv": 
      raise ValueError("Extension is wrong.")

    if not os.path.exists(file_name):
      raise FileNotFoundError("File not found.")

    
    return pd.read_csv(file_name) 

