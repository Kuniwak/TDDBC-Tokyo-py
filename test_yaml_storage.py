# coding: utf-8

from yaml_storage import YamlStorage
from task_collection import TaskCollection
from task import Task
from pathlib import Path
import unittest
import yaml


class TestYamlStorage(unittest.TestCase):
    @unittest.skip("別のテストを書きたくなった")
    def test_write_file(self):
        file_path = './.task_collection.yml'
        yaml_storage = YamlStorage(file_path)
        self.assertTrue(Path(file_path).exists())


    def test_to_yaml_with_empty_collection(self):
        task_collection = TaskCollection()
        yaml_str = YamlStorage.to_yaml(task_collection)

        expected = []

        self.assertEqual(yaml.load(yaml_str), expected)

    def test_to_yaml_with_not_empty_collection(self):
        task = Task('summary', 'desc')
        task_collection = TaskCollection()
        task_collection.append_task(task)

        yaml_str = YamlStorage.to_yaml(task_collection)

        expected = [{'summary': 'summary', 'description': 'desc'}]

        self.assertEqual(yaml.load(yaml_str), expected)
