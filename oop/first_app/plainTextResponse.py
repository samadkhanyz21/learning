from fastapi import FastAPI
# shows the test as plain text response rather than showing it as JSON response.
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get('/test', response_class=PlainTextResponse) # These are called endpoints for application. where are
# application sits.
def test_endpoint():
    return "Hello, This is a test."


@app.get('/', response_class=PlainTextResponse)
def home():
    return "welcome"
