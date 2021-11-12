from .models import *
from scripts.forms.form_factories import *

HilForm = model_form_factory(model_=HilModel, theme='atlantis')
TestCaseForm = model_form_factory(model_=TestCase, theme='atlantis')
HILsModalForm = model_form_factory(model_=HilModel, theme='atlantis_modal')
