"""Define the URL pattern of legal_toolkit"""

from django.urls import path

from . import views

app_name = 'legal_toolkit'
urlpatterns = [
    # Economic Compensation Tax Calculator page
    path('legal_toolkit/ect_calculator/', views.ect_calculator, name='ect_calculator'),
    # Sick Leave Salary Calculator page
    path('legal_toolkit/sls_calculator/', views.sls_calculator, name='sls_calculator'),
    # Days calculator page
    path('legal_toolkit/days_calculator/', views.days_calculator, name='days_calculator'),
    # Date calculator page
    path('legal_toolkit/date_calculator/', views.date_calculator, name='date_calculator'),
]
