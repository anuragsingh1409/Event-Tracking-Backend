from django.urls import path
from .views import EventAPIview
urlpatterns = [
    path("event/",EventAPIview.as_view()),
]

