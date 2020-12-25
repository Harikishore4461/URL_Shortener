from django.urls import path
from .views import Home, create, redirect

urlpatterns = [
	path('', Home, name="Home" ),
	path('url/<str:url>/', redirect, name="redirect"),
	path('create/', create, name="create")
]
