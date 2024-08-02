from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ManualListView.as_view(), name='manuals'),
    path('manual/<int:pk>/', manual_detail_view, name='manual_item'),
    path('manual_add/', CreateManual.as_view(), name='manual_add'),
    path('manual_add_file/', CreateManualFromFile.as_view(), name='manual_add_file'),
]
