import unittest
from task import Task


class TaskAssertion(unittest.TestCase):
    def assertTaskHasSummaryAndDescription(self, actual_task, expected_summary, expected_description):
        self.assertEqual(actual_task.summary, expected_summary)
        self.assertEqual(actual_task.description, expected_description)


class TestTask(TaskAssertion):
    def create_task(self, summary, description):
        task = Task(summary, description)
        return task


    def test_create_task_with_summary(self):
        summary = 'summary'
        desc = 'aaa'
        task = self.create_task(summary, desc)
        self.assertTaskHasSummaryAndDescription(task, summary, desc)


if __name__ == '__main__':
    unittest.main()
