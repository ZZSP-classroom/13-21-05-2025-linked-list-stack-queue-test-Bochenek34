import unittest
from hospital_1 import Queue, Patient

class TestHospitalQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()
        self.patient1 = Patient("Marek Woch", "10:00")
        self.patient2 = Patient("Grzegorz Braun", "11:00")
        self.queue.enqueue(self.patient1)
        self.queue.enqueue(self.patient2)

    def test_order(self):
        self.assertEqual(self.queue.peek(), self.patient1)

    def test_dequeue(self):
        removed = self.queue.dequeue()
        self.assertEqual(removed, self.patient1)
        self.assertEqual(self.queue.peek(), self.patient2)

if __name__ == '__main__':
    unittest.main()