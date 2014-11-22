import unittest
from task import Task


class TestTask(unittest.TestCase):
    def create_task(self, summary):
        task = Task(summary)
        return task


    def test_create_task_with_summary(self):
        summary = 'summary'
        task = self.create_task(summary)
        self.assertEqual(task.summary, summary)

    def test_create_task_with_summary2(self):
        summary = 'summary1'
        task = self.create_task(summary)
        self.assertEqual(task.summary, summary)


if __name__ == '__main__':
    unittest.main()
