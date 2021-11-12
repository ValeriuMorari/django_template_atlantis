from .models import HilModel
from scripts.tables.tables_factory import table_factory
from scripts.tables.extra_columns import Delete, Add
from scripts.tables.themes import Atlantis

HILsTable = table_factory(HilModel, parent_meta=Atlantis, extra_columns=[Delete, Add])
