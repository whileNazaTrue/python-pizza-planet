import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def parse_test_report(report_path):
    tree = ET.parse(report_path)
    root = tree.getroot()

    passed_tests = int(root.attrib.get('passed', '0'))
    failed_tests = int(root.attrib.get('failures', '0'))
    skipped_tests = int(root.attrib.get('skipped', '0'))

    return passed_tests, failed_tests, skipped_tests

def create_chart(passed, failed, skipped):
    labels = ['Passed', 'Failed', 'Skipped']
    values = [passed, failed, skipped]

    plt.bar(labels, values)
    plt.xlabel('Test Results')
    plt.ylabel('Number of Tests')
    plt.title('Integration Test Results')
    plt.savefig('chart.png')

# Read the report path from report.xml generated by pytest
report_path = 'report.xml'

# Parse the test report
passed_tests, failed_tests, skipped_tests = parse_test_report(report_path)

# Create the chart
create_chart(passed_tests, failed_tests, skipped_tests)
