import unittest
from task import Task


class TestTask(unittest.TestCase):
    def test_create_task(self):
        task = Task()
        self.assertIsInstance(task, Task)


if __name__ == '__main__':
    unittest.main()
