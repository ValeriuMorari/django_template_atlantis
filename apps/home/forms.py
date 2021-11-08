from .models import *
from scripts.forms.form_factories import *

HilForm = model_form_creator(model_=HilModel, theme='atlantis')
TestCaseForm = model_form_creator(model_=TestCase, theme='atlantis')
