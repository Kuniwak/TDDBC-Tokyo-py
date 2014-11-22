import yaml


class YamlStorage(object):
    def __init__(self, file_path):
        self.file_path = file_path

    @classmethod
    def to_yaml(cls, task_collection):
        task_list = [{'summary': task.summary, 'description': task.description} for task in task_collection]
        list(task_list)
        return yaml.dump(task_list)
