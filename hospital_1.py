class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, patient):
        self.items.append(patient)
    
    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)
    def peek(self):
        if not self.items:
            return None
        return self.items[0]
    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        return "\n".join(str(patient) for patient in self.items)


class Patient:
    def __init__(self, name, appointment_time):
        self.name = name
        self.appointment_time = appointment_time

    def __str__(self):
        return f"{self.name} at {self.appointment_time}"
    

if __name__ == '__main__':
    q = Queue()
    q.enqueue(Patient("Oskar", "10:00"))
    q.enqueue(Patient("marek", "13:00"))

    print("Next Patient: ", q.peek())
    print("all in queue: ")
    print(q)

    print("Calling next patient: ", q.dequeue())
    print("remaining in queue:")
    print(q)