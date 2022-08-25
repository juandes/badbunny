from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel

clf = load("model.joblib")
app = FastAPI()


class PredictionRequest(BaseModel):
    hour: int
    weekday: str


@app.post("/prediction")
def predict(req: PredictionRequest):
    # TODO: One hot encode the input
    prediction = clf.predict([[3, 0, 0, 0, 0, 1, 0, 0]])
    return {"prediction": int(prediction[0])}


@app.get("/model_information")
def model_information():
    return clf.get_params()


if __name__ == "__main__":
    print("running...")
