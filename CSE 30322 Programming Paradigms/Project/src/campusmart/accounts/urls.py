# urls.py

from django.urls import path
from .views import sign_up_view, login_view, logout_view

# Three pages for sign_up, login, and logout
urlpatterns = [
    path('sign_up/', sign_up_view, name="sign_up"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]