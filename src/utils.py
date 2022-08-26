"""
This file contains utils, i.e. the commonly used functions.
"""

import csv
try:
    from src.date_helper import date_in_n_days
except ImportError:
    print('ImportError')


def comp_avg(dict1):
    """
    Input:     dict1 (Dictionary of {date : float})
    Output:    average (float)
    """
    if len(dict1) == 0:
        return 0
    avg = sum(dict1.values())
    avg = avg/len(dict1)
    return avg



def read_csv_to_list(file_path):
    """
    Input:      path to CSV file (path)
    Output:     CSV as dictionary table/list (list of dictionaries)
    """
    file = open(file_path, newline='', encoding='utf-8')
    csv_file = csv.DictReader(file, delimiter=',', dialect='excel')
    csv_list = list(csv_file)
    file.close()
    return csv_list


def generate_sliding_window_csv(start, end, sys_time, n_slide_steps: int, slide_delta: int, sliding_window_file):
    """

    Creates the sliding window for the bitemporal data out of the following parameters:

    :param start: first start date, e.g. '2000-12-31'
    :param end: first end date, e.g. '2001-01-02'
    :param sys_time: first system date, e.g. '2001-01-03'
    :param n_slide_steps: (int) number of additional rows in window, e.g. 4
    :param slide_delta: (int) distance to previous window, e.g. 1

    :return: CSV table with 3 columns (w_start, w_end, w_system)

    """
    open(sliding_window_file, 'w').close() # make file empty
    f = open(sliding_window_file, 'a', encoding='utf-8', newline='')

    writer = csv.writer(f)

    row1 = 'w_start', 'w_end', 'w_system'
    row2 = start, end, sys_time
    writer.writerow(row1)
    writer.writerow(row2)

    for _ in range(n_slide_steps):
        start = date_in_n_days(date=start, n=slide_delta)
        end = date_in_n_days(date=end, n=slide_delta)
        sys_time = date_in_n_days(date=sys_time, n=slide_delta)

        row_i = start, end, sys_time
        writer.writerow(row_i)


    f.close()

