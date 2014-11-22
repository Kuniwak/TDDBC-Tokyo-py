# coding: utf-8

from yaml_storage import YamlStorage
from task_collection import TaskCollection
from pathlib import Path
import unittest


class TestYamlStorage(unittest.TestCase):
    @unittest.skip("別のテストを書きたくなった")
    def test_write_file(self):
        file_path = './.task_collection.yml'
        yaml_storage = YamlStorage(file_path)
        self.assertTrue(Path(file_path).exists())

    def test_to_yaml(self):


