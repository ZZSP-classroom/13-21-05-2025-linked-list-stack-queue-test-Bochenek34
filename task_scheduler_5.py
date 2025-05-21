class Task:
    def init(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority
        self.next = None

    def str(self):
        return f"{self.task_name} (Priority: {self.priority})"


class PriorityQueue:
    def init(self):
        self.head = None

    def add_task(self, task_name, priority):
        new_task = Task(task_name, priority)

        if self.head is None or self.head.priority < priority:
            new_task.next = self.head
            self.head = new_task
        else:
            current = self.head
            while current.next and current.next.priority >= priority:
                current = current.next
            new_task.next = current.next
            current.next = new_task

    def process_task(self):
        if self.head is None:
            return None
        highest_priority_task = self.head
        self.head = self.head.next
        return highest_priority_task

    def is_empty(self):
        return self.head is None

    def str(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(str(current))
            current = current.next
        return "\n".join(tasks)

