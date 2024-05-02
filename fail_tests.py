import json


def extract_failed_tests_names(report_file_path):
    failed_tests_names = []
    with open(report_file_path, 'r') as report_file:
        report_json = json.load(report_file)
        for test in report_json.get('tests', []):
            if test['outcome'] == 'failed':
                failed_tests_names.append(test['nodeid'])

    return ", ".join(failed_tests_names)


report_file = '.report.json'
failed_tests = extract_failed_tests_names(report_file)

print(failed_tests if failed_tests else "All tests passed")
