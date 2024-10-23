import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_1(self):
        time1 = data.Time(4, 9, 23)
        time2 = data.Time(9, 35, 40)
        expected = data.Time(13, 45, 4)
        actual = lab5.time_add(time1, time2)
        self.assertEqual(expected, actual)
    def test_time_add_2(self):
        time1 = data.Time(15, 35, 10)
        time2 = data.Time(0, 48, 40)
        expected = data.Time(16, 24, 50)
        actual = lab5.time_add(time1, time2)
        self.assertEqual(expected, actual)
    # Part 4
    def test_is_descending_1(self):
        list = [2, 5, 1, 9, 0, 3]
        expected = False
        actual = lab5.is_descending(list)
        self.assertEqual(expected, actual)
    def test_is_descending_2(self):
        list = [10.3, 9.2, 8.0, 7.4, 6.3, 5.0]
        expected = True
        actual = lab5.is_descending(list)
        self.assertEqual(expected, actual)

    # Part 5
    def test_largest_between_1(self):
        list = [4, 7, 3, 7, 1, 6, 3, 10, 2, 4]
        expected = 7
        actual = lab5.largest_between(list, 2, 8)
        self.assertEqual(expected, actual)
    def test_largest_between_2(self):
        list = [8, 4, 3, 6, 7]
        expected = None
        actual = lab5.largest_between(list, 1, 5)
        self.assertEqual(expected, actual)
    # Part 6
    def test_furthest_from_origin_1(self):
        list = [data.Point(10, 3), data.Point(9.2, 8.0), data.Point(7.4, 6.3), data.Point(5, 0)]
        expected = 1
        actual = lab5.furthest_from_origin(list)
        self.assertEqual(expected, actual)
    def test_furthest_from_origin_2(self):
        list = [data.Point(23, 78), data.Point(3, 5), data.Point(2, 93), data.Point(24, 13)]
        expected = 2
        actual = lab5.furthest_from_origin(list)
        self.assertEqual(expected, actual)
    def test_furthest_from_origin_3(self):
        list = []
        expected = None
        actual = lab5.furthest_from_origin(list)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
