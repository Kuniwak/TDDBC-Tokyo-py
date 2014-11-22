from task_collection import TaskCollection
from task import Task
import unittest


class TestTaskCollection(unittest.TestCase):
    def create_task_collection_has_a_task(self, opt_task=None):
        task_collection = TaskCollection()

        if opt_task:
            task = opt_task
        else:
            task = Task('summary', 'description')

        task_collection.append_task(task)
        return task_collection

    def test_create_task_collection(self):
        self.assertIsInstance(TaskCollection(), TaskCollection)

    def test_is_empty(self):
        task_collection = TaskCollection()
        self.assertTrue(task_collection.is_empty())

    def test_append_task(self):
        task_collection = self.create_task_collection_has_a_task()
        self.assertFalse(task_collection.is_empty())

    def test_get_last_task(self):
        task_collection = TaskCollection()
        self.assertEqual(task_collection.get_last_task(), None)

    def test_get_task_by_index_with_empty_collection(self):
        task_collection = TaskCollection()
        self.assertEqual(task_collection.get_task_by_index(0), None)

    def test_get_task_by_index_with_existent_index(self):
        task = Task('summary', 'desc')
        task_collection = self.create_task_collection_has_a_task(task)

        self.assertEqual(task_collection.get_task_by_index(0), task)

    def test_remove_task_by_index(self):
        task_collection = self.create_task_collection_has_a_task()

        task_collection.remove_task_by_index(0)
        self.assertTrue(task_collection.is_empty())

    def test_remove_task_by_index_with_unexistent_index(self):
        task_collection = self.create_task_collection_has_a_task()

        task_collection.remove_task_by_index(1)
        self.assertFalse(task_collection.is_empty())

    def test_is_available_index_with_unexistent_index(self):
        task_collection = TaskCollection()
        self.assertFalse(task_collection.is_available_index(0))

    def test_is_available_index_with_existent_index(self):
        task_collection = self.create_task_collection_has_a_task()
        self.assertTrue(task_collection.is_available_index(0))

    def test_iter_with_empty_collection(self):
        task_collection = TaskCollection()
        self.assertEqual(list(task_collection), [])

    def test_iter_with_not_empty_collection(self):
        task = Task('summary', 'desc')
        task_collection = self.create_task_collection_has_a_task(task)
        self.assertEqual(list(task_collection), [task])


if __name__ == '__main__':
    unittest.main()
