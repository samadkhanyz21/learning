from fastapi import FastAPI
# shows the app as JSON response rather than showing it as plain text response.
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()


@app.get('test_01', response_class=JSONResponse)
def test_endpoint():
    return {"test key 0": "value 0",
            "test key 1": "value 1",
            "test key 2": "value 2",
            3: "value 3", 4: 786}


@app.get('/', response_class=PlainTextResponse)
def home():
    return "Pakhair Rashe"
