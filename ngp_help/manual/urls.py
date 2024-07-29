from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ManualListView.as_view(), name='manuals'),
]
