import xml.etree.ElementTree as ET
import sys
import os

def parse_test_results(report_path):
    tree = ET.parse(report_path)
    root = tree.getroot()

    passed_tests = len(root.findall(".//testcase"))
    failed_tests = len(root.findall(".//testcase/failure"))
    skipped_tests = len(root.findall(".//testcase/skipped"))

    return passed_tests, failed_tests, skipped_tests

# Retrieve the path of the report.xml file generated by pytest
current_dir = os.getcwd()
report_path = os.path.join(current_dir, "report.xml")

passed_tests, failed_tests, skipped_tests = parse_test_results(report_path)

print(f'::set-output name=passed_tests::{passed_tests}')
print(f'::set-output name=failed_tests::{failed_tests}')
print(f'::set-output name=skipped_tests::{skipped_tests}')
