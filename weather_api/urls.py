from django.urls import path
from . import views
from .views import RegistrationView

urlpatterns = [
    path('weather_api/home.html', views.index, name="home"),
    path('', views.loginUser, name="login"),
    path('login', views.loginUser, name="login"),
    path('about', views.about, name="about"),
    path("result", views.result, name="result"),
    path('logout', views.logoutUser, name="logout"),
    path('register', RegistrationView.as_view(), name='register'),
    
    # path('social_links', views.social_links),
]
