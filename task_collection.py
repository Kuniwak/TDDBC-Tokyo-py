class TaskCollection(object):
    def __init__(self):
        self.task_list = []

    def is_empty(self):
        return self.task_list == []

    def append_task(self, task):
        self.task_list.append(task)

    def is_available_index(self, index):
        return len(self.task_list) > index >= 0

    def get_last_task(self):
        return self.get_task_by_index(len(self.task_list) - 1)

    def get_task_by_index(self, index):
        if not self.is_available_index(index):
            return None

        return self.task_list[index]

    def remove_task_by_index(self, index):
        if not self.is_available_index(index):
            return

        self.task_list.pop(index)
