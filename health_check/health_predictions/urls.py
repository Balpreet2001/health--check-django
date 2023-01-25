from django.urls import path
from .views import DiabetesView,HeartView
urlpatterns = [
    path('diabetes/',DiabetesView.as_view()),
    path('heart/',HeartView.as_view()),
]
