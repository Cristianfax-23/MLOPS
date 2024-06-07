from sklearn.model_selection import train_test_split , cross_validate , GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler , OrdinalEncoder
from sklearn.multiclass import OneVsRestClassifier
import pandas as pd
import utils
import numpy as np
import logging
import sys
import io
import warnings

warnings.filterwarnings('ignore')


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logger.info('Loading data ...')

try:

    data = pd.read_csv('data/Dry_Bean.csv')

except Exception as e:

    logger.error(f'Data has not been loaded')
    sys.exit(1)


logger.info('Loading model ...')

pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer()),
    ('scaler', StandardScaler()),
    ('classifier', OneVsRestClassifier(LogisticRegression(max_iter=10000)))
])

logger.info('Seraparating dataset into train and test')

X = data.drop("Class", axis=1)
Y = data["Class"]

logger.info('Coding classes ...') 

encoder = OrdinalEncoder()
datos_numericos = encoder.fit_transform(Y.values.reshape(-1,1))
Y = datos_numericos

Y = Y.astype(int)


X = pd.DataFrame(X)
Y = pd.DataFrame(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, shuffle=True , random_state=42)
logger.info('Looking for the best parameters')

param_grid = {
    'classifier__estimator__C': [0.001, 0.01, 0.1, 1, 10],
    'classifier__estimator__penalty': ['l1', 'l2'],
}


grid_search_lr = GridSearchCV(
    estimator = pipeline,
    param_grid = param_grid,
    cv = 10,
    n_jobs = -1,
    verbose = 1,
    scoring = 'accuracy'
    )

logger.info('Starting grid search... ') 

grid_search_lr.fit(X_train, Y_train)

best_score = grid_search_lr.best_score_
best_params = grid_search_lr.best_params_
model = grid_search_lr.best_estimator_

logger.info('Starting Cross Validation ... ')

final_result_train = cross_validate(model, X_train , Y_train , cv=10 )
final_result_test = cross_validate(model, X_test , Y_test , cv=10 )

train_score = np.mean(final_result_train['test_score'])
test_score = np.mean(final_result_test['test_score'])


try:

    assert train_score > 0.8
    assert test_score > 0.8

    logger.info('The model is efficient')

    logger.info(f'Score train : {train_score}')
    logger.info(f'Score test : {test_score}')

except:

    logger.error(f'The efficiency of the model is very low ')
    sys.exit(1)

logger.info('Updating model....')
utils.update_model(model)

logger.info('Generating model report...')
utils.save_metrics_report(train_score , test_score , model)

logger.info('Generating plot report...')

predict = model.predict(X_test)

utils.plot_metrics_report(Y_test , predict)

logger.info('Training Finished')



