from django.urls import path
from . import views

urlpatterns = [
    path('cidade/', views.CidadeList.as_view()),
    path('cidade/<int:pk>/', views.CidadeDetail.as_view())
]