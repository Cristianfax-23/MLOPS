from .utils import get_model , transform_dataframe
from .model import predict_model , input_model


model = get_model()

def get_predict(x : input_model):

    x = transform_dataframe(x)
    predict = model.predict(x)[0]

    if predict not in range(0,7):
        return -1


    return predict
