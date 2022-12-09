from django.urls import path
from . import views

urlpatterns = [
    path('<str:url>', views.ContView.as_view())
]

