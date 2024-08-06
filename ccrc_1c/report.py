from .types_and_constants import *
from .report_object import ReportObject
from .export_mask import ExportMask
from typing import List


def _get_report_file_line_level(line: str) -> int:
    return len(line) - len(line.lstrip()) - 1


class Report:
    def __init__(self, file_path: FilePath):
        self.path: Path = Path(file_path)
        self.children: List[Object] = []
        self.__load_from_file()

    def get_parent(self, level: int) -> 'Report':
        return self

    def add_child(self, child: 'ReportObject') -> 'ReportObject':
        self.children.append(child)
        return child

    def __load_from_file(self):
        with open(self.path, 'r') as file:
            current_level = 0
            parent_object = self
            for _ in range(6):
                file.readline()
            for line in file:
                strip_line = line.strip()
                if strip_line.startswith('- '):
                    level = _get_report_file_line_level(line)
                    if level <= current_level:
                        parent_object = parent_object.get_parent(current_level - level)
                        if parent_object is None:
                            raise 'Parent object not found'
                    current_level = level
                    if strip_line[2:5] in change_symbols:
                        changes_symbol = strip_line[2:5]
                        name = strip_line[5:]
                    elif strip_line[2] == '^':
                        changes_symbol = strip_line[2]
                        name = strip_line[3:]
                    else:
                        changes_symbol = ''
                        name = strip_line[2:]
                    parent_object = parent_object.add_child(ReportObject(parent_object, name, changes_symbol))
                else:
                    parent_object.changes.append(strip_line)

    def to_string(self, mask: 'ExportMask' = None) -> str:
        result = ('***- Объект изменен\n'
                  '-->- Объект присутствует только в конфигурации базы данных\n'
                  '<--- Объект присутствует только в конфигурации поставщика\n'
                  '^- Порядок объекта изменен\n\n')
        mask = mask if mask is not None else ExportMask()
        for child in self.children:
            result += child.to_string(mask)
        return result
