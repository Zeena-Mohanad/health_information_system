from ninja import Router
from account.schemas import UserInDB, UserOut, LoginData
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

auth_router = Router()

@auth_router.post("/signup", response=UserOut)
def signUp(request, user: UserInDB):
    try:
        user = User.objects.create_user(user.username, user.email, user.password)
        user.save()
        return UserOut(username=user.username, email=user.email)
    except Exception as e:
        return {"error": str(e)}


@auth_router.post("/login")
def signIn(request, data: LoginData):
    user = authenticate(request, username=data.username, password=data.password)
    if user is not None:
        login(request, user)
        return {"success": "User authenticated successfully."}
    else:
        return {"error": "Invalid credentials."}

@auth_router.post("/logout")
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return {"message": "User logged out successfully"}
    else:
        return {"message": "User is not logged in"}