from django.urls import path, include
from .views import add_client_data ,get_case_stats

urlpatterns = [
    path('addClientData/', add_client_data, name='add_client_data'),
    path('getCaseStats/', get_case_stats, name='get_case_stats'),

]