from django.urls import path
from .views import PersonListView, PersonDetailView

urlpatterns = [
    path('persons', PersonListView.as_view(), name='person_list'),
    path('persons/<int:person_id>', PersonDetailView.as_view(), name='person_detail'),
]
