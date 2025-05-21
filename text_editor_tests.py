import unittest
from text_editor_2 import Stack, TextEditor

class TestTextEditor(unittest.TestCase):

    def test_undo(self):
        editor = TextEditor()
        editor.type("Allo")
        editor.type(" Witam")
        self.assertEqual(editor.show(), "Allo Witam")
        editor.undo()
        self.assertEqual(editor.show(), "Allo")
        editor.undo()
        self.assertEqual(editor.show(), "")


if __name__ == '__main__':
    unittest.main()