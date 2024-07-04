import json

# Откройте JSON отчет pytest
with open('report.json') as f:
    report = json.load(f)

failed_tests = []

# Переберите все тесты в отчете
for test in report['tests']:
    if test['outcome'] == 'failed':
        test_name = test['nodeid']
        failure_reason = test['call']['longrepr']
        failed_tests.append(f"{test_name}\nПричина: {failure_reason}\n")

# Запишите информацию о проваленных тестах в файл
with open('failed_tests.txt', 'w') as f:
    if failed_tests:
        f.write("\n".join(failed_tests))
    else:
        f.write("Все тесты прошли успешно.")
