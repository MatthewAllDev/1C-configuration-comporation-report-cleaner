from __future__ import annotations
from typing import Union, TYPE_CHECKING
from pathlib import Path


if TYPE_CHECKING:
    from .report_object import ReportObject
    from .report import Report

FilePath = Union[str, Path]
Object = Union['Report', 'ReportObject']
change_symbols = {'-->', '***', '<--'}
MASK_INCLUDE = True
MASK_EXCLUDE = False
