from unittest import TestCase
from test_task.solution import into_minutes, free_time, number_of_chunks

class TestSolution(TestCase):

    def test_into_minutes(self):
        self.assertEqual(0, into_minutes("00:00"))
        self.assertEqual(29, into_minutes("00:29"))
        self.assertEqual(65, into_minutes("01:05"))
        self.assertEqual(90, into_minutes("01:30"))
    
    def test_free_time(self):
        busy = [
            {"start": 60, "stop": 120}
        ]
        start, stop = 0, 180
        self.assertEquals([60,60], free_time(start, stop, busy))
    
    def test_number_of_chunks(self):
        busy = [
            {"start": "10:00", "stop": "10:15"},
            {"start": "12:00", "stop": "12:30"}
        ]
        start, stop = "09:00", "14:00"
        chunk_size = 30

        self.assertEqual(8, number_of_chunks(busy, start=start, stop=stop, chunk_size=chunk_size))
    
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
        chunk_size = 30

        self.assertEqual(16, number_of_chunks(busy, start=start, stop=stop, chunk_size=chunk_size))