# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


from django.db import models


class HilModel(models.Model):
    objects = models.Manager()
    types = [('Dry', 'Dry'),
             ('Wet', 'Wet'),
             ('Unknown', 'Unknown')]
    had_architectures = [('HAD', 'HAD'),
                         ('NON-HAD', 'NON-HAD'),
                         ('Unknown', 'Unknown')]
    type = models.CharField(max_length=10, choices=types)
    had_architecture = models.CharField(max_length=10, choices=had_architectures)
    station = models.TextField(max_length=20)
    validation_spec = models.TextField()
    test_cases = models.TextField()
    variant_coding_test_case = models.TextField()
