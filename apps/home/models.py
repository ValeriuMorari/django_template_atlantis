# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from simple_history.models import HistoricalRecords

__all__ = ['TestCase', 'HilModel']


class TestCase(models.Model):
    objects = models.Manager()
    name = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def __repr__(self):
        return __class__.__name__


class HilModel(models.Model):
    objects = models.Manager()
    types = [('Dry', 'Dry'),
             ('Wet', 'Wet')]

    had_architectures = [('HAD', 'HAD'),
                         ('NON-HAD', 'NON-HAD')]

    hil_host = models.TextField(max_length=10, null=True)
    type = models.CharField(max_length=10, choices=types)
    had_architecture = models.CharField(max_length=10, choices=had_architectures)
    station = models.TextField(max_length=20)
    validation_spec = models.TextField()
    test_cases = models.ManyToManyField(TestCase, related_name='test_cases')
    variant_coding_test_cases = models.ManyToManyField(TestCase, related_name='variant_test_cases')
    history = HistoricalRecords()

    def __str__(self):
        return self.hil_host

    def __repr__(self):
        return __class__.__name__
