# Test task: Doctors hours

## description

A doctor accepts 30min appointments from 9AM to 9PM. During the day he/she takes breaks to eat, clean the cabinet, etc.

```
busy = [
            {"start": "10:30", "stop": "10:50"},
            {"start": "18:40", "stop": "18:50"},
            {"start": "14:40", "stop": "15:50"},
            {"start": "16:40", "stop": "17:20"},
            {"start": "20:05", "stop": "20:20"}
        ]
```
Requirement: form a list of open 30min windows

## solution

1. The implementation can be found in `test_task/solution.py`.
2. There are number of tests in `tests/test_solution.py`. One of those tests uses the schedule found above.
3. The code has no external dependencies. Only the python standard library is used. One can run them with `python run_tests.py`