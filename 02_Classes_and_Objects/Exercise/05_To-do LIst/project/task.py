class Task:
    comments = []
    completed = False

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date

    def change_name(self, new_name: str):
        if not new_name == self.name:
            self.name = new_name
            return self.name
        return f"Name cannot be the same."

    def change_due_date(self, new_date: str):
        if not new_date == self.name:
            self.due_date = new_date
            return self.due_date
        return "Date cannot be the same."

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number in range(len(self.comments)):
            for i in range(len(self.comments)):
                if i == comment_number:
                    self.comments[i] = new_comment
            return ', '.join(self.comments)

        return f"Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
