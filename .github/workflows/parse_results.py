import xml.etree.ElementTree as ET
import sys

def parse_test_results(report_path):
    tree = ET.parse(report_path)
    root = tree.getroot()

    passed_tests = len(root.findall(".//testcase"))
    failed_tests = len(root.findall(".//testcase/failure"))
    skipped_tests = len(root.findall(".//testcase/skipped"))

    return passed_tests, failed_tests, skipped_tests

report_path = sys.argv[1]
passed_tests, failed_tests, skipped_tests = parse_test_results(report_path)

print(f'::set-output name=passed_tests::{passed_tests}')
print(f'::set-output name=failed_tests::{failed_tests}')
print(f'::set-output name=skipped_tests::{skipped_tests}')
