class Section:
    def __init__(self, name: str):
        self.name = name
        self.task = []

    def add_task(self, new_task: Task):
        if new_task not in self.task:
            self.task.append(new_task)
            return f"Task {Task.details(new_task)} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        task = [el for el in self.task if el.name == task_name]
        if task:
            checked = task[0]
            checked.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        is_clear = [el for el in self.task if el.completed]
        cleared = len(is_clear)
        for el in is_clear:
            self.task.remove(el)
            return f"Cleared {cleared} tasks."
        return f"Cleared 0 tasks."

    def view_section(self):
        result = ""
        result += f"Section {self.name}:\n"
        for i in self.task:
            result += f"{i.details()}\n"
        return result
