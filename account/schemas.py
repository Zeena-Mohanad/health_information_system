from ninja import Schema

class UserInDB(Schema):
    username: str
    email: str
    password: str

class UserOut(Schema):
    username: str
    email: str
    
class LoginData(Schema):
    username: str
    password: str