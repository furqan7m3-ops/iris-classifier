from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Annotated
import joblib
import pandas as pd

class FlowerData(BaseModel):
    sepal_length: Annotated[float, Field(gt=0, description='Sepal length of the flower', example='5.1')]
    sepal_width: Annotated[float, Field(gt=0, description='Sepal width of the flower', example='3.5')]
    petal_length: Annotated[float, Field(gt=0, description='Petal length of the flower', example='1.4')]
    petal_width: Annotated[float, Field(gt=0, description='Petal width of the flower', example='0.2')]

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}

@app.post('/predict')
def predict(flowerData:FlowerData):
    flowerData = flowerData.model_dump()
    print(flowerData)
    test_df = pd.DataFrame(flowerData, index=[0])

    iris_model = joblib.load('iris_model.joblib')
    prediction = iris_model.predict(test_df)[0]
    return JSONResponse(status_code=200, content={'prediction': prediction})


