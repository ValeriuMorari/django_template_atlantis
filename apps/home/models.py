# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from simple_history.models import HistoricalRecords
from django.db import models
from django.contrib.auth.models import User
from CLdap.functions import get_last_user
from django.db.models.signals import post_save
from django.dispatch import receiver


__all__ = ['TestCase', 'HilModel', 'Profile']


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


class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sn = models.CharField(max_length=200)
    givenName = models.CharField(max_length=200)
    co = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    streetAddress = models.CharField(max_length=200)
    employeeID = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    manager = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    global_ExtensionAttribute26 = models.CharField(max_length=200)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user = get_last_user(instance.username)
        Profile.objects.create(user=instance,
                               title=getattr(user, 'title', 'unidentified field'),
                               sn=getattr(user, 'sn', 'unidentified field'),
                               givenName=getattr(user, 'givenName', 'unidentified field'),
                               co=getattr(user, 'co', 'unidentified field'),
                               department=getattr(user, 'department', 'unidentified field'),
                               company=getattr(user, 'company', 'unidentified field'),
                               streetAddress=getattr(user, 'streetAddress', 'unidentified field'),
                               employeeID=getattr(user, 'employeeID', 'unidentified field'),
                               mail=getattr(user, 'mail', 'unidentified field'),
                               manager=getattr(user, 'manager', 'unidentified field'),
                               mobile=getattr(user, 'mobile', 'unidentified field'),
                               global_ExtensionAttribute26=getattr(user, 'global-ExtensionAttribute26',
                                                                   'unidentified field'))


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

