# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('add_hil', views.HilManager.as_view(), name='add_hil'),
    path('add_test_case', views.TestCaseManager.as_view(), name='add_test_case'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
