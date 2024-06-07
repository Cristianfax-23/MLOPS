from sklearn.pipeline import Pipeline
from joblib import load
from pandas import DataFrame
import os

def get_model() -> Pipeline:
    
    path_model = os.environ.get( 'MODEL_PATH' , 'models/model.pkl')
    model = load(path_model)

    return model

def transform_dataframe(X) -> DataFrame:
    
    dictionario = {key : [value] for key , value in dict(X).items()}
    dataframe = DataFrame(dictionario) 

    return dataframe

def transform_class(a):
    class_mapping = {
    0 :'BARBUNYA' ,
    1 : 'BOMBAY' ,
    2 : 'CALI',
    3 : 'DERMASON',
    4 : 'HOROZ',
    5 : 'SEKER',
    6 : 'SIRA'
    }

    result = class_mapping[a]

    return result