class TaskCollection(object):
    def __init__(self):
        self.task_list = []

    def is_empty(self):
        return self.task_list == []

    def append_task(self, task):
        self.task_list.append(task)

    def get_last_task(self):
        if self.task_list:
            return self.task_list[-1]
        return None
