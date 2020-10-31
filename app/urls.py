from django.urls import path
from app.views import mutter_detail, mutter_list

urlpatterns = [
    path('', mutter_list, name='mutter_list'),
    path('detail/<int:mutter_id>', mutter_detail, name='mutter_detail'),
]
