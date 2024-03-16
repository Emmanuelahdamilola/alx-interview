#!/usr/bin/python3
"""
A program to ingest and track logs, periodically printing statistics.
"""


from sys import stdin, exit


def print_code_tracking(total_file_size, code_tracker):
    """
    Print formatted log statistics.
    """
    # Print total size of data passed to date
    print('File size: ' + str(total_file_size))

    code_list = sorted(code_tracker.keys())

    # Print formatted count of requests by status code
    for code in code_list:
        if code_tracker[code] != 0:
            print(code + ': ' + str(code_tracker[code]))


code_tracker = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
total_file_size = 0
loop_counter = 0

try:
    for line in stdin:
        # Pull necessary fields from log line
        line_split = line.split()

        if len(line_split) >= 2:
            status_code, file_size = [part for part in line_split[-2:]]

            # Update persistent size and status counters
            total_file_size += int(file_size)
            if status_code in code_tracker:
                code_tracker[status_code] += 1

                # Keep track of how many logs have been read in print loop
                if loop_counter == 9:
                    print_code_tracking(total_file_size, code_tracker)
                    loop_counter = 0
                else:
                    loop_counter += 1

    # Print stats at end of input stream
    print_code_tracking(total_file_size, code_tracker)

except KeyboardInterrupt:
    print_code_tracking(total_file_size, code_tracker)
