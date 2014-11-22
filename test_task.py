import unittest
from task import Task


class TestTask(unittest.TestCase):
    def test_create_task(self):
        task = Task()
        self.assertIsInstance(task, Task)

    def test_create_task_with_summary(self):
        summary = 'summary'
        task = Task(summary)
        self.assertEqual(task.summary, summary)

    def test_create_task_with_summary2(self):
        summary = 'summary1'
        task = Task(summary)
        self.assertEqual(task.summary, summary)


if __name__ == '__main__':
    unittest.main()
