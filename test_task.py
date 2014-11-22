import unittest
from task import Task


class TestTask(unittest.TestCase):
    def test_create_task(self):
        task = Task()
        self.assertIsInstance(task, Task)

    def test_create_task_with_summary(self):
        task = Task('summary')
        self.assertEqual(task.summary, 'summary')

    def test_create_task_with_summary2(self):
        task = Task('summary1')
        self.assertEqual(task.summary, 'summary1')


if __name__ == '__main__':
    unittest.main()
