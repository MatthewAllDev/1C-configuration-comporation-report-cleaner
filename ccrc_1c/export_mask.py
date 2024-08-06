from .types_and_constants import *
from typing import *


class ExportMask:
    def __init__(self,
                 object_names: List[str] = None,
                 object_change_types: List[str] = None,
                 max_level: int = 999,
                 mask_type: bool = MASK_EXCLUDE):
        self.object_names = object_names if object_names is not None else []
        self.object_change_types = object_change_types if object_change_types is not None else []
        self.max_level = max_level
        self.mask_type = mask_type

    def match(self, report_object: 'ReportObject', level: int = 0) -> bool:
        if level > self.max_level:
            return False
        in_mask = report_object.name in self.object_names or report_object.changes_symbol in self.object_change_types
        if self.mask_type == MASK_INCLUDE:
            return in_mask
        else:
            return not in_mask
