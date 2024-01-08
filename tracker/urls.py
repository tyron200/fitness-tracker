# tracker/urls.py
from django.urls import path
from .views import dashboard, add_workout, user_login, user_logout

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('add_workout/', add_workout, name='add_workout'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
