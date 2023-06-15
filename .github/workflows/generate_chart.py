import matplotlib.pyplot as plt
import sys

def create_chart(passed, failed, skipped):
    labels = ['Passed', 'Failed', 'Skipped']
    values = [passed, failed, skipped]

    plt.bar(labels, values)
    plt.xlabel('Test Results')
    plt.ylabel('Number of Tests')
    plt.title('Integration Test Results')
    plt.savefig('chart.png')

passed_tests = int(sys.argv[1])
failed_tests = int(sys.argv[2])
skipped_tests = int(sys.argv[3])

create_chart(passed_tests, failed_tests, skipped_tests)
