from django.urls import path
from . import views

urlpatterns = [
    path('weather_api/home.html', views.index, name="home"),
    path('', views.loginUser, name="login"),
    path('login', views.loginUser, name="login"),
    path("result", views.result, name="result"),
    path('logout', views.logoutUser, name="logout"),
    # path('social_links', views.social_links),
]
