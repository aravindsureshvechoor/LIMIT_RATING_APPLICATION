from django.urls import path
from .views import (CreateCriteriaView,CriteriasUpdateAPIView,CriteriasDeleteAPIView,CriteriasListAPIView)

urlpatterns = [
    path('createcriteria/',CreateCriteriaView.as_view(),name='create_criteria'), 
    path('updatecriteria/<int:criteria_id>/', CriteriasUpdateAPIView.as_view(), name='update_criteria'),
    path('deletecriteria/<int:pk>/', CriteriasDeleteAPIView.as_view(), name='delete_criteria'),
    path('retrievecriterias/', CriteriasListAPIView.as_view(), name='retrieve_criterias'),
]