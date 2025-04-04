
# Unit tests for data reading 
import pytest 
from utils.readers import CSVReader



def test_file_name(): 
    file_name = 123

    with pytest.raises(TypeError) as err: 
        CSVReader.read(file_name)

def test_file_not_found():
    file_name = "not_existent.csv" 

    with pytest.raises(FileNotFoundError): 
        CSVReader.read(file_name) 

def test_extension(): 
    file_name = "test_file_name.parquet" 

    with pytest.raises(ValueError): 
        CSVReader.read(file_name)



    