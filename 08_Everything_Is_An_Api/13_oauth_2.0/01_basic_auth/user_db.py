from typing import TypedDict

class userdb_dict(TypedDict):
    username:str
    full_name:str
    email:str
    hashed_password:str
    disabled: bool | None



fake_users_db : dict[str,userdb_dict] = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

