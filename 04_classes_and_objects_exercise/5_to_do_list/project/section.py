class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = list()

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task_name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        current_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        return f'Cleared {current_len - len(self.tasks)} tasks.'

    def view_section(self):
        view = list()
        view.append(f'Section {self.name}:')
        for task in self.tasks:
            view.append(task.details())
        return '\n'.join(view)
