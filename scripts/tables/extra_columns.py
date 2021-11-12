import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.tables import Table
from django_tables2.utils import A
from abc import abstractmethod, ABCMeta


class AbstractExtraColumnMeta(ABCMeta, Table):
    pass


class AbstractExtraColumn:
    __metaclass__ = AbstractExtraColumnMeta

    @property
    @abstractmethod
    def accessor(self):
        pass

    @staticmethod
    @abstractmethod
    def render_accessor(record):
        raise NotImplementedError("Please reference existing button class")

    @abstractmethod
    def __str__(self):
        return __class__.__name__


class Delete(AbstractExtraColumn):

    accessor = tables.Column(accessor=A('pk'), verbose_name='Delete')

    @staticmethod
    def render_accessor(record):
        return format_html('<button class="btn btn-default"><a href="delete/{id}/">Delete</a></button>', id=record.id)

    def __str__(self):
        return __class__.__name__


class Add(AbstractExtraColumn):

    accessor = tables.Column(accessor=A('pk'), verbose_name='Add')

    @staticmethod
    def render_accessor(record):
        return format_html('<button class="btn btn-default"><a href="delete/{id}/">Add</a></button>', id=record.id)

    def __str__(self):
        return __class__.__name__
