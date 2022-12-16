from django.urls import path
from . import views

urlpatterns = [
    path('<str:urlpath>', views.ContView.as_view())
]

