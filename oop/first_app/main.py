from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class User(BaseModel):
    username: str
    shrt_descrpt: str
    liked_posts: Optional[list[int]] = None # Optional sets the tone that this variable is not mendatory.


# This function gives you all info on web page
def get_user_info() -> (str, str): # Here we are just defining the typing style not necessary.

    """
    This tells us that the function is of what type and after
    conversion what its type will be, known as typing.
    """
    contant = {
        'username': 'testUser',
        'shrt_descrpt': 'My Bio'
    }
    return User(**contant)

# Here all the mechanism for creating an API is written
@app.get("/user/me", response_model=User)

def test_endpoint():

    user = get_user_info()

    return user