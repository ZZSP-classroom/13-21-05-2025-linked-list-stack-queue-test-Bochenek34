import unittest
from call_center_4 import CallCenter, Call

class TestCallCenter(unittest.TestCase):

    def setUp(self):
        self.center = CallCenter()
        self.center.receive_call("ID1", "09:00")
        self.center.receive_call("ID2", "09:05")

    def test_receive_call(self):
        call = self.center.incoming_queue.dequeue()
        self.assertEqual(call.caller_id, "ID1")
        self.assertEqual(call.time_received, "09:00")

    def test_process_call(self):
        self.center.process_call()
        self.assertFalse(self.center.processing_stack.is_empty())

    def test_complete_call(self):
        self.center.process_call()
        completed = self.center.complete_call()
        self.assertEqual(completed.caller_id, "ID1")
        self.assertTrue(self.center.processing_stack.is_empty())

if __name__ == '__main__':
    unittest.main()