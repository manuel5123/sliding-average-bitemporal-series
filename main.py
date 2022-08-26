"""
In this file/module you find the command line handling and the main function for the sliding window average.
"""

try:
    from src.utils import read_csv_to_list, generate_sliding_window_csv, comp_avg
except ImportError:
    print('ImportError')

import sys
import csv



def main_func(csv_list, w_start, w_end, w_system):
    """
    Input:     csv_list (List), w_start (date), w_end (date), w_system (date)
    Output:    values in window (Dictionary of dates,floats), average (float)

    :param csv_list: (List) csv data
    :param w_start:  (date)
    :param w_end:  (date)
    :param w_system:  (date)
    :return: Dict of date-data-values, and average of these data-values

    The input series (csv_list) is sorted along the "system" time index (ascending).
    """
    reversed_csv_list = reversed(csv_list)  # reversed iterator
    date_data_dict = {}
    for row in reversed_csv_list:
        if (row['sys'] <= w_system) and (w_start <= row['valid'] <= w_end) and (row['valid'] not in date_data_dict):
            date_data_dict[row['valid']] = float(row['data'])
    average = comp_avg(dict1=date_data_dict)
    return date_data_dict, average




if __name__ == '__main__':
    arg_list = sys.argv[1:]
    print('\n', 'arg_list = ', arg_list, '\n')
    if len(arg_list) == 5:
        w_start = arg_list[0]
        w_end = arg_list[1]
        w_system = arg_list[2]
        n_steps = int(arg_list[3])
        delta = int(arg_list[4])
    else:
        w_start = '2000-12-31'
        w_end = '2001-01-02'
        w_system = '2001-01-03'
        n_steps = 4
        delta = 1

    # generate the sliding window CSV
    path_to_generated_sliding_window = 'generated_files/generated_sliding_window.csv'
    generate_sliding_window_csv(start=w_start,end=w_end,sys_time=w_system, n_slide_steps=n_steps, slide_delta=delta, sliding_window_file=path_to_generated_sliding_window)

    sliding_window = read_csv_to_list(file_path=path_to_generated_sliding_window)

    path_bitemporal_series_data = 'Files/bitemporal_series.csv'
    csv_list_data = read_csv_to_list(file_path=path_bitemporal_series_data)

    path_generated_output = 'generated_files/generated_output.csv'
    open(path_generated_output, 'w').close() # make file empty
    f = open(path_generated_output, 'a', encoding='utf-8', newline='')    
    writer = csv.writer(f)

    row1 = 'sys', 'valid', 'data'
    writer.writerow(row1)

    for entry in sliding_window:
        date_data_dict1, average1 = main_func(csv_list=csv_list_data, w_start=entry['w_start'], w_end=entry['w_end'], w_system=entry['w_system'])
        print(date_data_dict1, average1)
        writer.writerow([entry['w_system'], entry['w_end'], average1])
    f.close()

