from ccrc_1c import Report, ExportMask
from easygui import fileopenbox, msgbox, filesavebox


def start():
    report_file_path = fileopenbox('', 'Выберите файл отчета для обработки', '*.txt', ['*.txt'])
    if report_file_path is None:
        msgbox('Отчет не выбран', 'Ошибка')
        return
    report = Report(report_file_path)
    output_file_path = filesavebox('',
                                   'Выберите файл для сохранения результатов', './report.txt', ['*.txt'])
    names = ['Справочная информация', 'Обработка.МониторыРуководителя', 'Макет - Изменено']
    change_types = ['-->']
    export_mask = ExportMask(names, change_types)
    with open(output_file_path, 'w') as file:
        file.write(report.to_string(export_mask))


if __name__ == "__main__":
    start()
