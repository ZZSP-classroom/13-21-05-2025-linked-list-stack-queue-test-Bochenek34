class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, operation):
        self.items.append(operation)
    
    def pop(self):
        if not self.items:
            return None
        return self.items.pop()
    
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]
    
    def __str__(self):
        return "\n".join(reversed(self.items))
    
class TextEditor:
    def __init__(self):
        self.content = ""
        self.undo_stack = Stack()

    def type(self, text):
        self.undo_stack.push(self.content)
        self.content += text

    def undo(self):
        last_state = self.undo_stack.pop()
        if last_state is not None:
            self.content = last_state

    def show(self):
        return self.content
    

if __name__ == '__main__':
    editor = TextEditor()
    editor.type("Allo")
    editor.type("Witam")
    print(editor.show())