from fastapi import FastAPI
from .app.model import input_model , predict_model
from .app.utils import get_model , transform_dataframe , transform_class
from .app.views import get_predict

model = get_model()

app = FastAPI(docs_url='/')

@app.post("/v1/predict")

def predict(data : input_model):

    x = transform_dataframe(data)
    x = get_predict(x)
    x = transform_class(x)

    return x
