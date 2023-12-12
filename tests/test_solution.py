from unittest import TestCase
from test_task.solution import into_minutes, into_hh_mm, free_time, list_of_open_windows

class TestSolution(TestCase):

    def test_into_minutes(self):
        self.assertEqual(0, into_minutes("00:00"))
        self.assertEqual(29, into_minutes("00:29"))
        self.assertEqual(65, into_minutes("01:05"))
        self.assertEqual(90, into_minutes("01:30"))
    
    def test_into_hh_mm(self):
        self.assertEqual("00:00", into_hh_mm(0))
        self.assertEqual("00:50", into_hh_mm(50))
        self.assertEqual("01:15", into_hh_mm(75))
        self.assertEqual("01:05", into_hh_mm(65))

    def test_free_time(self):
        busy = [
            {"start": 60, "stop": 120}
        ]
        start, stop = 0, 180
        expected = [
            {"start": 0, "stop": 60},
            {"start": 120, "stop": 180}]

        self.assertEquals(expected, list(free_time(start, stop, busy)))
    
    def test_list_of_open_windows(self):
        busy = [
            {"start": "10:00", "stop": "10:15"},
            {"start": "12:00", "stop": "12:30"}
        ]
        start, stop = "09:00", "13:00"
        window_size = 30
        expected = [
            {"start": "09:00", "stop": "09:30"},
            {"start": "09:30", "stop": "10:00"},
            {"start": "10:15", "stop": "10:45"},
            {"start": "10:45", "stop": "11:15"},
            {"start": "11:15", "stop": "11:45"},
            {"start": "12:30", "stop": "13:00"}
        ]

        self.assertEqual(expected, list_of_open_windows(busy, start=start, stop=stop, window_size=window_size))

    ##################################################
    ######## TEST TASK ###############################
    ##################################################
    def test_task(self):
        busy = [
            {"start": "10:30", "stop": "10:50"},
            {"start": "18:40", "stop": "18:50"},
            {"start": "14:40", "stop": "15:50"},
            {"start": "16:40", "stop": "17:20"},
            {"start": "20:05", "stop": "20:20"}
        ]
        start, stop = "09:00", "21:00"
        window_size = 30
        expected = [
            {"start": "09:00", "stop": "09:30"},
            {"start": "09:30", "stop": "10:00"},
            {"start": "10:00", "stop": "10:30"},
            {"start": "10:50", "stop": "11:20"},
            {"start": "11:20", "stop": "11:50"},
            {"start": "11:50", "stop": "12:20"},
            {"start": "12:20", "stop": "12:50"},
            {"start": "12:50", "stop": "13:20"},
            {"start": "13:20", "stop": "13:50"},
            {"start": "13:50", "stop": "14:20"},
            {"start": "15:50", "stop": "16:20"},
            {"start": "17:20", "stop": "17:50"},
            {"start": "17:50", "stop": "18:20"},
            {"start": "18:50", "stop": "19:20"},
            {"start": "19:20", "stop": "19:50"},
            {"start": "20:20", "stop": "20:50"},
        ]

        self.assertEqual(expected, list_of_open_windows(busy, start=start, stop=stop, window_size=window_size))