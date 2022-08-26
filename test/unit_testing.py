import unittest

import os
import sys
sys.path.append(os.getcwd()) # to avoid ImportError

try:
    from src.date_helper import date_in_n_days, date_next_day, return_date_next_day
    from src.utils import comp_avg
except ImportError:
    print('error')



class TestDates(unittest.TestCase):
    def test_dates_n_days(self):
        result = date_in_n_days(date='2020-02-28', n=12)
        self.assertEqual(result, '2020-03-11')

    def test_next_day(self):
        self.assertEqual(date_next_day('2001-12-31'), '2002-01-01')
    
    def test_next_date(self):
        res = ('2020', '02', '29')
        self.assertEqual(return_date_next_day('2020', '02', '28', True),res)


class TestUtils(unittest.TestCase):
    def test_avg(self):
        test_dict = {
            'date1': 13,
            'date2': 1.5,
            'date3': 12.5
        }
        avg = comp_avg(test_dict)
        self.assertEqual(avg, 9)







if __name__ == '__main__':
    unittest.main()

