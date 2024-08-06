from .types_and_constants import *
from typing import List


class ReportObject:
    def __init__(self, parent: 'ReportObject', name: str, changes_symbol: str):
        self.parent = parent
        self.name = name
        self.changes_symbol = changes_symbol
        self.children: List[Object] = []
        self.changes: List[str] = []

    def add_child(self, child: 'ReportObject') -> 'ReportObject':
        self.children.append(child)
        return child

    def get_parent(self, level: int) -> 'ReportObject':
        parent_object = self.parent
        while level > 0:
            parent_object = parent_object.parent
            level -= 1
        return parent_object

    def to_string(self, mask, level: int = 0) -> str:
        if not mask.match(self, level):
            return ''
        head = f'{"\t" * level}- {self.changes_symbol}{self.name}\n'
        body = ''
        for change in self.changes:
            body += f'{"\t" * (level + 1)}{change}\n'
        for child in self.children:
            body += child.to_string(mask, level + 1)
        return head + body if body != '' or not len(self.children) else ''

    def __str__(self):
        return f'{self.changes_symbol}{self.name}'
