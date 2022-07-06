from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('case_1', views.case1, name='case_1'),
    path('case_2', views.case2, name='case_2'),
    path('case_3', views.case3, name='case_3'),
    path('case_4', views.case4, name='case_4'),
    path('case_5', views.case5, name='case_5'),
    path('case_6', views.case6, name='case_6'),
    path('case_7', views.case7, name='case_7'),
    path('case_8', views.case8, name='case_8'),
]
