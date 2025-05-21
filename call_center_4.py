class Call:
    def __init__(self, caller_id, time_received):
        self.caller_id = caller_id
        self.time_received = time_received

    def __str__(self):
        return f"Call from {self.caller_id} at {self.time_received}"


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, call):
        self.items.append(call)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0


class Stack:
    def __init__(self):
        self.items = []

    def push(self, call):
        self.items.append(call)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


class CallCenter:
    def __init__(self):
        self.incoming_queue = Queue()
        self.processing_stack = Stack()

    def receive_call(self, caller_id, time_received):
        self.incoming_queue.enqueue(Call(caller_id, time_received))

    def process_call(self):
        call = self.incoming_queue.dequeue()
        if call:
            self.processing_stack.push(call)
        return call

    def complete_call(self):
        return self.processing_stack.pop()

