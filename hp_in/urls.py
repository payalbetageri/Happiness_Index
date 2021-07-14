from django.urls import path
from . import views

urlpatterns = [
        path('',views.home,name='home'),
        path('gdc/',views.gdc,name='country'),
        path('lsr',views.lsr,name='ladder_score'),
        path('gdc_result',views.gdc_result,name='gdc_result'),
        path('lsr_result',views.lsr_result,name='lsr_result')
        ]
