from django.urls import path
from .views import Login,Registration,Logout
urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('register/',Registration.as_view(),name='register'),
    path('logout/',Logout.as_view(),name='logout'),
]
