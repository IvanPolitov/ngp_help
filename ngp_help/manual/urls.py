from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ManualListView.as_view(), name='manuals'),
    path('manual/<int:pk>/', ManualDetailView.as_view(), name='manual_item'),
]
