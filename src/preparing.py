import pandas as pd
import numpy as np
import logging
import io
import sys
from sklearn.preprocessing import OrdinalEncoder
from imblearn.under_sampling import RandomUnderSampler
from io import StringIO
from dvc import api

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level= logging.INFO,
    datefmt= '%H:%M:S',
    stream=sys.stderr
)


logger = logging.getLogger(__name__)

logger.info('Loading data ...')

try:

    logger.info('Connection with the s3 bucket ...')

    path_data = api.get_url( path= 'data/Dry_Bean.csv' , remote= 'aws-bucket-data')

    data = pd.read_csv(path_data)
    logger.info('Data read successfully ...')

except Exception as e:
    logger.error(f'Could not find file Dry_Bean.csv: {e}')

num_class = dict(data.Class.value_counts())

distant = lambda x , y : np.abs(x - y)

logger.info('Balancing classes ...') 
if data.Class.value_counts().min() > 250:
    for i , nu_a in num_class.items():
        for b , nu_b in num_class.items():

            if distant(nu_a , nu_b) > 100:

                rus = RandomUnderSampler(random_state=42)
                X = data.drop("Class",axis=1)
                Y = data['Class'] 
                X_over, y_over = rus.fit_resample(X,Y)
                data = pd.concat([X_over, y_over], axis=1)
                break
        

data = pd.DataFrame(data)

data.to_csv('data/Dry_Bean.csv' ,index=False)

logger.info('The data has been prepared correctly')


