from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from account import views
from account.views import UserListView, SearchhView

# router = routers.DefaultRouter()
# router.register('api/message', LoginViewSet, basename="message")

urlpatterns =[
    path('search', UserListView.as_view()),
    path('searchh', SearchhView.as_view()),
]