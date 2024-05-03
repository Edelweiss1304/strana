# импортирование модуля json
import json


# определение функции для извлечения имен упавших тестов
def extract_failed_tests_names(report_file_path):
    # инициализация пустого списка для имён упавших тестов
    failed_tests_names = []
    # открытие файла отчета как report_file в режиме чтения ('r')
    with open(report_file_path, 'r') as report_file:
        # загрузка данных JSON из report_file в report_json
        report_json = json.load(report_file)
        # перебор каждого теста в поле "tests" из report_json
        for test in report_json.get('tests', []):
            # проверка, если исход теста равен 'failed'
            if test['outcome'] == 'failed':
                # добавление идентификатора теста в список failed_tests_names
                failed_tests_names.append(test['nodeid'])
    # возврат полученных имён упавших тестов, соединенных запятой
    return failed_tests_names


# основная часть скрипта
if __name__ == "__main__":
    # путь к файлу отчета .report.json
    report_file = '.report.json'
    # вызов функции извлечения упавших тестов и помещение результатов в failed_tests
    failed_tests = extract_failed_tests_names(report_file)
    # открытие (или создание) файла failed_tests.txt в режиме записи ('w')
    with open('failed_tests.txt', 'w') as f:
        # проверка, есть ли упавшие тесты в failed_tests
        if failed_tests:
            # запись строки "Упавшие тесты: " и имен упавших тестов в файл
            f.write("Упавшие тесты: " + ", ".join(failed_tests))
        else:
            # запись строки "Все тесты пройдены" в файл, если упавших тестов нет
            f.write("Все тесты пройдены")
