from task_collection import TaskCollection
from task import Task
import unittest


class TestTaskCollection(unittest.TestCase):
    def test_create_task_collection(self):
        self.assertIsInstance(TaskCollection(), TaskCollection)

    def test_is_empty(self):
        task_collection = TaskCollection()
        self.assertTrue(task_collection.is_empty())

    def test_append_task(self):
        task_collection = TaskCollection()
        task_collection.append_task(Task('summary', 'description'))
        self.assertFalse(task_collection.is_empty())

    def test_get_last_task(self):
        task_collection = TaskCollection()
        self.assertEqual(task_collection.get_last_task(), None)

if __name__ == '__main__':
    unittest.main()
